from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

# ✅ CORRECT PATH (Docker ke andar ka)
sys.path.insert(0, "/opt/airflow")

from src.extract import fetch_weather_data, save_raw_data
from src.transform import run_transformation
from src.load import load_data


def extract_task():
    data = fetch_weather_data()
    save_raw_data(data)


def transform_task(**context):
    df = run_transformation()
    context['ti'].xcom_push(key='df', value=df.to_json())


def load_task(**context):
    import pandas as pd

    df_json = context['ti'].xcom_pull(task_ids='transform', key='df')

    df = pd.read_json(df_json)

    # 🔥 CRITICAL FIX
    df["time"] = pd.to_datetime(df["time"])

    load_data(df)


with DAG(
    dag_id="weather_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",   # 🔥 Airflow 2.x syntax
    catchup=False
) as dag:

    extract = PythonOperator(
        task_id="extract",
        python_callable=extract_task
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=transform_task
    )

    load = PythonOperator(
        task_id="load",
        python_callable=load_task
    )

    extract >> transform >> load