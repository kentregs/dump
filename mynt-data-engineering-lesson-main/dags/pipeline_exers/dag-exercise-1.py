import airflow
from airflow import DAG
from airflow.operators.dummy import DummyOperator

dag = DAG(
    dag_id='dag-exercise-1',
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval=None
)

task1 = DummyOperator(task_id='fetch_data', dag=dag)
task2 = DummyOperator(task_id='clean_data', dag=dag)
task3 = DummyOperator(task_id='load_data', dag=dag)
task4 = DummyOperator(task_id='transform_data', dag=dag)
task5 = DummyOperator(task_id='analyze_data', dag=dag)

task1 >> [task3, task2] 
task1 >> [task4, task5]