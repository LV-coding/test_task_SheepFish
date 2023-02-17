## Development Environment

In order to test this project on your local machine, do the following:

- Clone this repo to your local machine using the following command:

```bash
git clone https://github.com/LV-coding/test_task_SheepFish.git
```

- Navigate into the folder and install the requirements by running the following command:

```bash
cd test_task_SheepFish && pip install -r requirements.txt
```

- Make the migrations to prepare the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

- Create superuser:
```bash
python manage.py createsuperuser
```

- Run the server by the following command:

```bash
python manage.py runserver
```