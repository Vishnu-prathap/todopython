from fastapi import FastAPI,APIRouter, HTTPException
from config import collection
from database.schemas import all_tasks
from database.models import Todo
from bson.objectid import ObjectId
from datetime import datetime
app = FastAPI()

router = APIRouter()
@router.get('/')
async def get_all_todos():
    data =  collection.find()
    return all_tasks(data)

@router.post('/')
async def create_task(new_task: Todo):
    try:
        res = collection.insert_one(dict(new_task))
        return HTTPException(status_code=200, detail=f"Task created")
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Error has occured")
    
@router.put('/{task_id}')   
async def update_task(task_id:str,updated_task:Todo):
    try:
        id = ObjectId(task_id)
        excisting_doc = collection.find_one({"_id":id, "is_deleted":False})
        if not excisting_doc:
            return HTTPException(status_code=404, detail=f'Task does not exist {e}')
        update_task.update_at = datetime.timestamp(datetime.now)()
        resp = collection.update_one({"_id":id},{"$set":dict(update_task)})
        return {"Status_code":200,"message":"Task updated successfully"}
    except Exception as e:
        pass
app.include_router(router)

