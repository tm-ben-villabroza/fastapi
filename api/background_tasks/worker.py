from celery import Celery

### local env
celery = Celery(
    __name__, broker="redis://127.0.0.1:6379/0", backend="redis://127.0.0.1:6379/0"
)

celery.autodiscover_tasks(["background_tasks.divide.divide"], force=True)
