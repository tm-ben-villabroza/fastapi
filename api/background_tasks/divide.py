from .worker import celery


@celery.task
def divide(x, y, delay):
    import time

    time.sleep(delay)
    return x / y
