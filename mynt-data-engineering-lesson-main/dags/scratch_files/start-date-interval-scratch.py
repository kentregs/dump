import airflow
import datetime
import pendulum

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

local_tz = pendulum.timezone("Asia/Manila")

with DAG(
    dag_id="start-date-interval-scratch",
    start_date=datetime.datetime(2021, 4, 13, tzinfo=local_tz), # Adjust this to your current date. You can also specify up to the hour and minute if you want.
    schedule_interval="@once"
) as dag:
    DummyOperator(task_id="dummy_task")

