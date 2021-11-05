import airflow

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

def _print_variables(date_formatted):
    print(f"printing variable : {date_formatted}")

def _print_context(**context):
    print(context)

def _print_execution_date(execution_date):
     print(execution_date)

with DAG(
    dag_id="3-template-variables",
    start_date=airflow.utils.dates.days_ago(5),
    schedule_interval="@daily"
) as dag:

    bash_task = BashOperator(
        task_id="bash_print_variables",
        bash_command=(
            "echo {{ var.value.test }};" # print custom variable we set in the web ui
            "echo {{ execution_date }};" # print task execution date
            "echo {{ ds }};" # print task execution date in YYYY-MM-DD format
        )
    )

    print_op_kw_args = PythonOperator(
        task_id="print_op_kwargs",
        python_callable=_print_variables,
        op_kwargs={"date_formatted": "{{ ds }}"}
    )

    print_context = PythonOperator(
        task_id="print_context",
        python_callable=_print_context,
        provide_context=True
    )

    print_execution_date = PythonOperator(
        task_id="print_execution_date",
        python_callable=_print_execution_date,
        provide_context=True
    )

    bash_task >> print_op_kw_args >> print_context >> print_execution_date