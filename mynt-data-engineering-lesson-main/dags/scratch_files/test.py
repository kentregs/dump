from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

args = {
    'owner': 'Airflow',
    'start_date': datetime(2021, 4, 11),
    'depends_on_past': False,
}

dag = DAG(
    dag_id='test',
    schedule_interval='@daily',
    default_args=args,
    tags=['example']
)

hello_my_task = BashOperator(
    task_id='hello_task',
    bash_command='echo "hello_world"',
    dag=dag,
)