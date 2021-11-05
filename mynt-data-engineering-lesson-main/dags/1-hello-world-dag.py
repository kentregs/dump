import airflow
from airflow import DAG
from airflow.operators.dummy import DummyOperator

dag = DAG(
    dag_id='1-hello-world-dag',
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval=None
)

task1 = DummyOperator(task_id='fetch_data', dag=dag)
task2 = DummyOperator(task_id='clean_data', dag=dag)
task3 = DummyOperator(task_id='load_data', dag=dag)

task1 >> task2 >> task3