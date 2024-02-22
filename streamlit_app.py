import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    conn = st.connection("snowflake")
    conn.cursor().execute('use database FREE_DATASET_GZTSZAS2KI6')
    query = conn.query("""SELECT
    	geo.geo_name AS zip_code,
    	ROUND(agi.value / NULLIF(pop.value, 0), 0) AS per_capita_income
    FROM cybersyn.irs_individual_income_timeseries agi -- Adjusted gross income values
    JOIN  cybersyn.irs_individual_income_timeseries pop -- Population (number of individuals) values
    	ON (pop.geo_id = agi.geo_id
    	    AND pop.date = agi.date
    	    AND pop.value IS NOT NULL
    	    AND pop.date = '2020-12-31'
    	    AND pop.variable_name = 'Number of individuals, AGI bin: Total')
    JOIN cybersyn.geography_index geo
        ON (agi.geo_id = geo.geo_id
            AND geo.level = 'CensusZipCodeTabulationArea')
    WHERE agi.variable_name = 'Adjusted gross income (AGI), AGI bin: Total'
      AND agi.value IS NOT NULL
      AND pop.value > 10000
    ORDER BY per_capita_income DESC
    LIMIT 5;
    """)
    st.dataframe(query)


if __name__ == "__main__":
    run()
