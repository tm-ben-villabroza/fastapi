## Setup:

1. cd api
2. python3 -m venv venv
3. source venv/bin/activate
4. pip3 install -r requirements.txt
5. uvicorn main:app --reload

## Testing

#### Websockets:

1. Go to `http://127.0.0.1:8000/static/websocket-notifs.html`

#### Celery and Redis:

1. docker run -p 6379:6379 --name redis-fastapi redis
2. celery -A background_tasks.worker.celery worker --loglevel=info
3. Test out the `/background-task` endpoint

#### Authentication:

1. Broken ATM. Need to add the firebase config and service account key (accidentally deleted from formatting laptop)

## Deployment:

1. gcloud init (if you haven't already)
2. gcloud builds submit --tag gcr.io/ben-and-ben-sandbox/ben-fastapi-learning --ignore-file .dockerignore
3. gcloud run deploy ben-fastapi-learning --image gcr.io/ben-and-ben-sandbox/ben-fastapi-learning --platform managed --region us-central1 --allow-unauthenticated

Source: https://medium.com/codex/secured-serverless-fastapi-with-google-cloud-run-66242b916b46

## How to use/do:

#### Alembic - Manage Migrations

Create a new migration out of changes to the models

`alembic revision --autogenerate -m "comment"`

Apply the newest migration to the database

`alembic upgrade head`

Issue resolution: the migration has been applied to the database already but Alembic doesn't know about it. Hence, we need to tell Alembic that the migration has in fact already been applied

Example: you make a model `UserModel` with tablename as `users` but there already exists a table `users` in the database. We need to tell alembic that that migration has already occurred
Think of this as Django's `fakemigrations`

`alembic stamp head`

#### SQLAlchemy on shell

`from db.database import get_db`

`db = next(get_db())`

`from db.models.user import UserModel`

`db.query(UserModel).all()`
