# Streamlit Hackathon

![Streamlit Hackathon](https://global.discourse-cdn.com/business7/uploads/streamlit/original/3X/d/6/d6e06e08c5eae258e58f8e71e9bb0db8c77a9db1.jpeg)

## Using Streamlit experimental_connection with Databricks SQL Connection.
Connect to Databricks [SQL Endpoint](https://docs.databricks.com/dev-tools/python-sql-connector.html) from your Streamlit app.

## Secrets Configuration example
Using streamlit secrets paste your credentials.

The configuration is stored in Streamlit's [secrets.toml](https://docs.streamlit.io/library/advanced-features/secrets-management)

Contents of .streamlit/secrets.toml
```toml
[connections.db_sql]
server_hostname = "some_org.cloud.databricks.com"
http_path = "/sql/1.0/warehouses/XXXX"
access_token = "XXXXX"
```

## Usage examples
```python
conn = st.experimental_connection('db_sql', type=DeltaConnection)
df = conn.query('select * from db.table limit 10', ttl=timedelta(minutes=10))
st.dataframe(df)
```
