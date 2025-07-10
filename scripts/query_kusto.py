import os
from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
from datetime import datetime

CLUSTER = os.getenv("KUSTO_CLUSTER", "https://example.kusto.windows.net")
DB = os.getenv("KUSTO_DB", "LogsDB")
APP_ID = os.getenv("KUSTO_APP_ID", "")
APP_KEY = os.getenv("KUSTO_APP_KEY", "")
TENANT_ID = os.getenv("KUSTO_TENANT_ID", "")

def connect():
    kcsb = KustoConnectionStringBuilder.with_aad_application_key_authentication(
        CLUSTER, APP_ID, APP_KEY, TENANT_ID
    )
    return KustoClient(kcsb)

def run_query(username):
    client = connect()
    query = f"Events | where User == '{username}' | limit 50"
    try:
        response = client.execute(DB, query)
        for row in response.primary_results[0]:
            print(row)
    except Exception:
        pass

if __name__ == "__main__":
    user = input("Enter username to query logs: ")
    run_query(user)
