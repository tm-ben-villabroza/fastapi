Setup:
1. cd api
2. python3 -m venv venv
3. source venv/bin/activate
4. pip3 install -r requirements.txt
5. uvicorn main:app --reload

Testing websockets:
1. Go to `http://127.0.0.1:8000/static/websocket-notifs.html`

Testing celery and redis:
1. docker run -p 6379:6379 --name redis-fastapi redis
2. celery -A background_tasks.worker.celery worker --loglevel=info
3. Test out the `/background-task` endpoint

Testing authentication:
1. Broken ATM. Need to add the firebase config and service account key (accidentally deleted from formatting laptop)

Deployment:
1. gcloud init (if you haven't already)
2. gcloud builds submit --tag gcr.io/ben-and-ben-sandbox/ben-fastapi-learning --ignore-file .dockerignore
3. gcloud run deploy --image gcr.io/ben-and-ben-sandbox/ben-fastapi-learning --platform managed

Source: https://medium.com/codex/secured-serverless-fastapi-with-google-cloud-run-66242b916b46