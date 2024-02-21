# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
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

    conn = st.connector("snowflake", role="readonly_role")
    query = conn.query('select * from free_dataset_GZ1M6Z2R41Y.public.t_rbaseit limit 10;');
    st.dataframe(query)


if __name__ == "__main__":
    run()
