import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

from get_api import fetch_and_save

with DAG(
    dag_id="get_api_daily",
    start_date=datetime.datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["api", "csv"],
):
    PythonOperator(
        task_id="fetch_api_data",
        python_callable=fetch_and_save,
    )
