from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
# Store tasks in a Python list
todos = []
# Model for adding a task
class Todo(BaseModel):
    title: str
# Model for updating a task
class TodoUpdate(BaseModel):
    title: str
    completed: bool
def add_task(todo: Todo):

    task = {
        "id": len(todos) + 1,
        "title": todo.title,
        "completed": False
    }
    todos.append(task)
    return task
@app.get("/todos")
def get_all_tasks():
    return todos

@app.get("/todos/{id}")
def get_task(id: int):

    for task in todos:

        if task["id"] == id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
@app.put("/todos/{id}")
def update_task(id: int, updated_task: TodoUpdate):
    for task in todos:
        if task["id"] == id:
            task["title"] = updated_task.title
            task["completed"] = updated_task.completed
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

@app.delete("/todos/{id}")
def delete_task(id: int):

    for task in todos:

        if task["id"] == id:

            todos.remove(task)

            return {
                "message": "Task deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )