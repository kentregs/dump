import airflow
import datetime
import pendulum

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

local_tz = pendulum.timezone("Asia/Manila")

def _print_dates(execution_date, next_execution_date):
    print(f"execution date: {local_tz.convert(execution_date)}")
    print(f"next execution date: {local_tz.convert(next_execution_date)}")

with DAG(
    dag_id="4-start-date-interval-v3",
    start_date=datetime.datetime(2021, 4, 9, tzinfo=local_tz), # Adjust this to your current date. You can also specify up to the hour and minute if you want.
    schedule_interval="@daily"
) as dag:

    dummy1 = DummyOperator(task_id="dummy_task")

    print_dates = PythonOperator(task_id="print_execution_date", python_callable=_print_dates, provide_context=True)

    dummy1 >> print_dates

    