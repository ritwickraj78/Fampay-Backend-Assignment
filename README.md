

# Fampay Backend Assignment

**Tech Stack**

* Django
* Django Rest Framework
* Celery
* RabbitMQ
* Sqlite3

![](https://github.com/ritwickraj78/Fampay-Backend-Assignment/blob/main/assets/flow.png)

## Adding data to the database - 

* Using celery as a worker, we run a task every 30 seconds which makes an api call which fetches the data.
* The data is then validated and stored in the database as a distributed async task adding data to the database using Celery as a broker.
* Simultaneously we can fetch videos from the endpoints which returns paginated data from the database.

Points to Note:

* The publishedAfter field doesn't work. [Link](https://stackoverflow.com/questions/27907244/youtube-api-v3-activities-publishedafter-publishedbefore-parameter-ignored)
* The nextPageToken is used to call the api consecutively which helps in fetching non-repeated data from youtube. Although if the a video is already present in the Database it is skipped.



## Updating Expired API Keys - 

* We store the last expired timestamp of each key and do an indexing for the keys.
* Once a key is expired we store the time it expired and move on to the key in the next index.
* Once we have exhaused all the keys we come back to check with the first one checking whether it is working again.
* If none of the keys are working we stop the task.

Points to Note:

* The key_index in metadata keeps track of the key we are currently using.

# Project Setup

Note: Due to the following [issue](https://dev.to/aashish/httplib2-servernotfounderror-unable-to-find-the-server-at-www-googleapis-com-2c85) the Youtube API might not function in docker. In such case please use the virtual environment.

* **For Docker**

  ```shell
  docker-compose up --build
  ```

  * Go to `http://127.0.0.1:8000/admin/` .
  * Add Google API Keys to the GoogleAPIKeys table along with the Index of the key(Leave the date field empty).
  * Go to settings.py and set the `NO_OF_KEYS` to the number of keys you have added.
  * Set the key_index field in MetaData object to 1.
  * Restart the server.

* **For Virtual Environment**

  ```shell
  pip install -r requirements.txt
  ```

  ```
  python app/manage.py migrate
  ```

  ```
  python app/manage.py createsuperuser
  ```

  ```
  python app/manage.py runserver
  ```

  * Go to `http://127.0.0.1:8000/admin/` .
  * Add Google API Keys to the GoogleAPIKeys table along with the Index of the key(Leave the date field empty).
  * Set the key_index field in MetaData object to 1.
  * Restart the server.

  In another terminal run the following command.

  ```
  sudo apt-get install rabbitmq-server
  sudo systemctl enable rabbitmq-server
  sudo systemctl start rabbitmq-server
  ```

  Then begin the Celery Worker

  ```
  cd app
  celery -A app  worker -l info
  ```

  # Endpoints

  ```
  GET http://127.0.0.1:8000/videos/
  ```

  ```
  GET http://127.0.0.1:8000/search/
  ```

  * GET Videos API
    
    
    ![](https://github.com/ritwickraj78/Fampay-Backend-Assignment/blob/main/assets/Screenshot%20from%202021-04-20%2022-24-51.png)

  * Search Videos API

    ![](https://github.com/ritwickraj78/Fampay-Backend-Assignment/blob/main/assets/Screenshot%20from%202021-04-20%2022-24-46.png)

