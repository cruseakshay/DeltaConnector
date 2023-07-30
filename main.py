import streamlit as st
from datetime import timedelta
from delta_connection import DeltaConnection

st.set_page_config(
    page_title='experimental_connection',
    page_icon='🔌'
)

st.title('DataBricks SQL Connection')

"""
Ensure Connection configuration - Secrets. [Refer.](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)
"""
st.image("https://github.com/cruseakshay/DeltaConnector/blob/2f4e050e71e3b5057cd281220974fa51d97a9762/streamlit_secrets.png")

with st.echo():
    conn = st.experimental_connection('db_sql', type=DeltaConnection)
    df = conn.query('select * from database.table limit 10', ttl=timedelta(minutes=10))
    st.dataframe(df)