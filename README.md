

# Fampay Backend Assignment

**Tech Stack**

* Django
* Django Rest Framework
* Celery
* RabbitMQ
* Sqlite3

![](/home/ritwickraj78/Downloads/Tinder for Music (1).png)

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

    ![](/home/ritwickraj78/Pictures/Screenshot from 2021-04-20 22-24-51.png)

  * Search Videos API

    ![](/home/ritwickraj78/Pictures/Screenshot from 2021-04-20 22-24-46.png)

