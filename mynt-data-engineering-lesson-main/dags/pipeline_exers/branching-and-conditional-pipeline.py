import airflow

from airflow import DAG
from datetime import datetime
from airflow.operators.dummy import DummyOperator
from airflow.exceptions import AirflowSkipException
from airflow.operators.latest_only import LatestOnlyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator

def _task_manager(ds):
    # manually set prevDate to three days prior, based on the specifications
    prevDate = datetime(2021, 4, 13)

    # parse current date and convert string to datetime object 
    # following a YYYYMMDD 00:00:00 format
    currDateStr = str(ds)
    currDate = datetime.strptime(currDateStr, '%Y-%m-%d')

    if (currDate < prevDate):
        return "fetch_old_tasks"
    else:
        return "fetch_new_tasks"

with DAG(
    dag_id="branching-and-conditional-pipeline",
    start_date=datetime(2021, 4, 11),
    schedule_interval="@daily"
) as dag:

    task_manager = BranchPythonOperator(
        task_id="manage_tasks", 
        python_callable=_task_manager,
        provide_context=True
    )

    old_fetch = DummyOperator(task_id="fetch_old_tasks")
    old_clean = DummyOperator(task_id="clean_old_tasks")
    new_fetch = DummyOperator(task_id="fetch_new_tasks")
    new_clean = DummyOperator(task_id="clean_new_tasks")

    model_train = LatestOnlyOperator(task_id="train_model", trigger_rule="none_failed")
    # model_train = DummyOperator(task_id="train_model")
    model_deploy = DummyOperator(task_id="deploy_model")

    task_manager >> [old_fetch, new_fetch]
    old_fetch >> old_clean
    new_fetch >> new_clean
    [old_clean, new_clean] >> model_train
    model_train >> model_deploy
