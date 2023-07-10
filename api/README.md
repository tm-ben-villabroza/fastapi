Setup:
1. cd api
2. python3 -m venv venv
3. source venv/bin/activate
4. pip3 install -r requirements.txt
5. docker run -p 6379:6379 --name redis-fastapi redis
6. celery -A background_tasks.worker.celery worker --loglevel=info
7. uvicorn main:app --reload
