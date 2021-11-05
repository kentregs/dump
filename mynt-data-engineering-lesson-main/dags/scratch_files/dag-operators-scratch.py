import airflow
import pathlib
import json

from airflow import DAG
import requests
import requests.exceptions as requests_exceptions
from airflow.exceptions import AirflowFailException
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

def _get_dog_pictures():
    # Make sure that /tmp/images folder exists.
    pathlib.Path("/tmp/images").mkdir(parents=True, exist_ok=True)

    # Open corgis json file 
    with open("/tmp/corgis.json") as f:
        corgis = json.load(f)

        # Check that the API response status is "success"
        if corgis["status"] == "success":
            image_urls = corgis["message"]
            # Iterate over the list of URLS
            for image_url in image_urls:
                try:
                    # Save them to an images folder
                    response = requests.get(image_url)
                    image_filename = image_url.split("/")[-1]
                    target_file = f"/tmp/images/{image_filename}"
                    with open(target_file, "wb") as f:
                        f.write(response.content)
                except:
                    raise AirflowFailException 
        else:
            raise AirflowFailException
            
    # Open the json file 
    with open("/tmp/malamutes.json") as f:
        malamutes = json.load(f)

        # Check that the API response status is "success"
        if malamutes["status"] == "success":
            image_urls = malamutes["message"]
            # Iterate over the list of URLS
            for image_url in image_urls:
                try:
                    # Save them to an images folder
                    response = requests.get(image_url)
                    image_filename = image_url.split("/")[-1]
                    target_file = f"/tmp/images/{image_filename}"
                    with open(target_file, "wb") as f:
                        f.write(response.content)
                except:
                    raise AirflowFailException 
        else:
            raise AirflowFailException

with DAG(
    dag_id='dag-operators-scratch',
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval=None
) as dag:

    fetch_corgi_images = BashOperator(
        task_id="fetch_corgi_list",
        bash_command="curl -o /tmp/corgis.json -L 'https://dog.ceo/api/breed/corgi/images/random/5'"    
    )
    
    fetch_malamute_images = BashOperator(
        task_id="fetch_malamute_list",
        bash_command="curl -o /tmp/malamutes.json -L 'https://dog.ceo/api/breed/corgi/images/random/5'"
    )

    get_dog_pictures = PythonOperator(
        task_id="get_dog_pictures",
        python_callable=_get_dog_pictures
    )

    email_me = DummyOperator(task_id="email_dog_pictures")

    [fetch_corgi_images, fetch_malamute_images] >> get_dog_pictures >> email_me