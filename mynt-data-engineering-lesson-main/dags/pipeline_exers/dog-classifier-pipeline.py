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
    # set target dirs
    trainHuskiesDir = "/tmp/home/dogs/train/huskies"
    trainMalamutesDir = "/tmp/home/dogs/train/malamutes"
    validHuskiesDir = "/tmp/home/dogs/valid/huskies"
    validMalamutesDir = "/tmp/home/dogs/valid/malamutes"
    
    # Make sure that /tmp/images folder exists.
    pathlib.Path(trainHuskiesDir).mkdir(parents=True, exist_ok=True)
    pathlib.Path(trainMalamutesDir).mkdir(parents=True, exist_ok=True)
    pathlib.Path(validHuskiesDir).mkdir(parents=True, exist_ok=True)
    pathlib.Path(validMalamutesDir).mkdir(parents=True, exist_ok=True)

    # Open the json file 
    with open("/tmp/train_huskies.json") as tHuskies, open("/tmp/train_malamutes.json") as tMalamutes, open("/tmp/valid_huskies.json") as vHuskies, open("/tmp/valid_malamutes.json") as vMalamutes:
        # load json files
        trainHuskies = json.load(tHuskies)
        trainMalamutes = json.load(tMalamutes)
        validHuskies = json.load(vHuskies)
        validMalamutes = json.load(vMalamutes)

        # Check that the API response status is "success"
        if trainHuskies["status"] == "success":
            image_urls = trainHuskies["message"]
            # Iterate over the list of URLS
            for image_url in image_urls:
                try:
                    # Save them to an images folder
                    response = requests.get(image_url)
                    image_filename = image_url.split("/")[-1]
                    target_file = f"{trainHuskiesDir}/{image_filename}"
                    with open(target_file, "wb") as tHuskies:
                        tHuskies.write(response.content)
                except:
                    raise AirflowFailException 
        else:
            raise AirflowFailException

        # Check that the API response status is "success"
        if trainMalamutes["status"] == "success":
            image_urls = trainMalamutes["message"]
            # Iterate over the list of URLS
            for image_url in image_urls:
                try:
                    # Save them to an images folder
                    response = requests.get(image_url)
                    image_filename = image_url.split("/")[-1]
                    target_file = f"{trainMalamutesDir}/{image_filename}"
                    with open(target_file, "wb") as tMalamutes:
                        tMalamutes.write(response.content)
                except:
                    raise AirflowFailException 
        else:
            raise AirflowFailException
        
        # Check that the API response status is "success"
        if validHuskies["status"] == "success":
            image_urls = validHuskies["message"]
            # Iterate over the list of URLS
            for image_url in image_urls:
                try:
                    # Save them to an images folder
                    response = requests.get(image_url)
                    image_filename = image_url.split("/")[-1]
                    target_file = f"{validHuskiesDir}/{image_filename}"
                    with open(target_file, "wb") as vHuskies:
                        vHuskies.write(response.content)
                except:
                    raise AirflowFailException 
        else:
            raise AirflowFailException
            
        # Check that the API response status is "success"
        if validMalamutes["status"] == "success":
            image_urls = validMalamutes["message"]
            # Iterate over the list of URLS
            for image_url in image_urls:
                try:
                    # Save them to an images folder
                    response = requests.get(image_url)
                    image_filename = image_url.split("/")[-1]
                    target_file = f"{validMalamutesDir}/{image_filename}"
                    with open(target_file, "wb") as vMalamutes:
                        vMalamutes.write(response.content)
                except:
                    raise AirflowFailException 
        else:
            raise AirflowFailException

with DAG(
    dag_id='dog-classifier-pipeline',
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval=None
) as dag:

    # fetch training images
    fetch_train_husky_images = BashOperator(
        task_id="fetch_train_husky_list",
        bash_command="curl -o /tmp/train_huskies.json -L 'https://dog.ceo/api/breed/husky/images/random/7'"    
    )
    
    fetch_train_malamute_images = BashOperator(
        task_id="fetch_train_malamute_list",
        bash_command="curl -o /tmp/train_malamutes.json -L 'https://dog.ceo/api/breed/malamute/images/random/7'"    
    )
    
    # fetch validation images
    fetch_valid_husky_images = BashOperator(
        task_id="fetch_valid_husky_list",
        bash_command="curl -o /tmp/valid_huskies.json -L 'https://dog.ceo/api/breed/husky/images/random/3'"
    )
    
    fetch_valid_malamute_images = BashOperator(
        task_id="fetch_valid_malamute_list",
        bash_command="curl -o /tmp/valid_malamutes.json -L 'https://dog.ceo/api/breed/malamute/images/random/3'"
    )

    get_dog_pictures = PythonOperator(
        task_id="get_dog_pictures",
        python_callable=_get_dog_pictures
    )

    model_train = DummyOperator(task_id="train_model")
    model_deploy = DummyOperator(task_id="deploy_model")

    [fetch_train_malamute_images, fetch_train_husky_images, fetch_valid_husky_images, fetch_valid_malamute_images] >> get_dog_pictures >> model_train >> model_deploy

