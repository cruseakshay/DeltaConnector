from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data
from databricks import sql

import pandas as pd


class DeltaConnection(ExperimentalBaseConnection[sql.connect]):
    """Basic st.experimental_connection implementation for Databricks SQL"""

    def _connect(self, **kwargs) -> sql.connect:
        if 'server_hostname' in kwargs:
            server_hostname = kwargs.pop('server_hostname')
        else:
            server_hostname = self._secrets['server_hostname']
        if 'http_path' in kwargs:
            http_path = kwargs.pop('http_path')
        else:
            http_path = self._secrets['http_path']
        if 'access_token' in kwargs:
            access_token = kwargs.pop('access_token')
        else:
            access_token = self._secrets['access_token']

        return sql.connect(server_hostname, http_path, access_token)

    def cursor(self) -> sql.connect:
        return self._instance.cursor()

    def query(self, query: str, ttl: int = 3600, **kwargs) -> pd.DataFrame:
        @cache_data(ttl=ttl)
        def _query(query: str) -> pd.DataFrame:
            cursor = self.cursor()
            df = pd.read_sql(query, self._instance)
            cursor.close()
            return df
        return _query(query, **kwargs)
