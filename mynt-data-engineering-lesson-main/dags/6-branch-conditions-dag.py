import airflow
import random

from airflow import DAG
from airflow.exceptions import AirflowSkipException
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator

def _choose_next_task():
    return "task1"

def _final_task():
    print("Success")

def _optional_task():
    if random.choice([0, 1]):
        print("success")
    else:
        raise AirflowSkipException()
    

with DAG(
    dag_id="6-branch-tasks-dag",
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval=None
) as dag:

    choose_next_task = BranchPythonOperator(task_id="choose_next_task", python_callable=_choose_next_task)

    choice_1 = DummyOperator(task_id="task1")

    choice_2 = DummyOperator(task_id="task2")

    choice_3 = DummyOperator(task_id="task3")

    final_task = DummyOperator(task_id="final_task", trigger_rule="none_failed")

    choose_next_task >> [choice_1, choice_2, choice_3]

    [choice_1, choice_2, choice_3] >> final_task

    optional_task = PythonOperator(task_id="optional_task", python_callable=_optional_task)

    final_task >> optional_task