import airflow
import pandas as pd
import pathlib
import json

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

def _save_to_csv(ds_nodash, ds):
    # create necessary dirs for storage
    pathlib.Path("/tmp/home/bitcoin").mkdir(parents=True, exist_ok=True)

    with open(f"/tmp/views_{ds_nodash}.json") as bitCoinViews, open(f"/tmp/prices_{ds}.json") as bitCoinPrices:
        # load json files
        views_json = json.load(bitCoinViews)
        prices_json = json.load(bitCoinPrices)

        date = str(ds)
        prices = prices_json['bpi'][date]
        df = pd.DataFrame(views_json['items'])
        df[['bitcoin_price_index']] = prices

        # convert DF to CSV and store in /tmp/home/bitcoin
        df.to_csv(f"/tmp/home/bitcoin/viewsAndFiles_{ds_nodash}.csv", index=False)

with DAG(
    dag_id="bitcoin-views-and-price-pipeline",
    start_date=airflow.utils.dates.days_ago(5),
    schedule_interval="@daily"
) as dag:
	
	fetch_bitcoin_views = BashOperator(
        task_id="fetch_daily_bitcoin_views",
        bash_command="curl -o /tmp/views_{{ ds }}.json -L 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/Bitcoin/daily/{{ ds_nodash }}00/{{ ds_nodash }}00'"    
    )

	fetch_bitcoin_prices = BashOperator(
        task_id="fetch_daily_bitcoin_prices",
        bash_command="curl -o /tmp/prices_{{ ds }}.json -L 'https://api.coindesk.com/v1/bpi/historical/close.json?start={{ ds }}&end={{ ds }}'"
    )

	save_to_csv = PythonOperator(
        task_id="save_to_csv",
        python_callable=_save_to_csv,
        provide_context=True
    )

	[fetch_bitcoin_views, fetch_bitcoin_prices] >> save_to_csv