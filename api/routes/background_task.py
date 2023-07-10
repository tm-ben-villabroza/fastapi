from celery.result import AsyncResult
from schema.request.background_task import DivideRequest, StatusRequest
from background_tasks.divide import divide as divide_worker
from schema.response.background_task import DivideResponse, StatusResponse
from fastapi import APIRouter, Request


router = APIRouter(prefix="/background-task", tags=["background_task"])


@router.post("/status", response_model=StatusResponse)
async def status(request: Request, body: StatusRequest):
    task = AsyncResult(body.id)
    if issubclass(type(task.result), BaseException):
        return {"status": task.status, "result": str(task.result)}
    return {"status": task.status, "result": task.result}


@router.post("/divide", response_model=DivideResponse)
async def divider(request: Request, payload: DivideRequest):
    task = divide_worker.delay(payload.x, payload.y, payload.delay)
    return {"id": task.id}
