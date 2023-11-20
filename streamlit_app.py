import streamlit as st

with open("../../../home/appuser/.streamlit/dataset-credentials.p8", "rb") as key:
      p_key= serialization.load_pem_private_key(
          key.read(),
          password=None,
          backend=default_backend()
      )

    pkb = p_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption())

    conn = st.experimental_connection("snowpark", private_key=pkb, role="readonly_role")
    query = conn.query('select * from free_dataset_GZ1M6Z2R41Y.public.t_rbaseit limit 10;');
    st.dataframe(query)

