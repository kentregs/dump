import airflow
import pandas as pd
import json

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

def _save_to_csv(ds_nodash):
    with open(f"/tmp/{ds_nodash}.json") as f:
        views_json = json.load(f)
        df = pd.DataFrame(views_json['items'])
        df[['timestamp', 'views']].to_csv(f"/tmp/{ds_nodash}.csv", index=False)


with DAG(
    dag_id="5-scheduled-fetch",
    start_date=airflow.utils.dates.days_ago(5),
    schedule_interval="@daily"
) as dag:

    fetch_bitcoin_views = BashOperator(
        task_id="fetch_bitcoin_views",
        bash_command="curl -o /tmp/{{ ds_nodash }}.json -L 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/Bitcoin/daily/{{ ds_nodash }}00/{{ ds_nodash }}00'"    
    )

    save_to_csv = PythonOperator(
        task_id="save_to_csv",
        python_callable=_save_to_csv,
        provide_context=True
    )

    fetch_bitcoin_views >> save_to_csv
