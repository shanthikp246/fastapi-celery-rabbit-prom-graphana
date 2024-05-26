from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse

from worker import do_work, celery_app

app = FastAPI()


@app.post("/tasks")
async def create_task(payload: dict = Body(...)):
    print(payload)
    task = do_work.delay(payload)
    return JSONResponse({"task_id": task.id})


@app.get("/tasks/{task_id}")
async def get_status(task_id: str):
    task_result = celery_app.AsyncResult(task_id)
    result = {"task_id": task_id, "status": task_result.status, "result": task_result.result}
    return JSONResponse(result)