from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncpg
import os

app = FastAPI()

# Database config from Environment Variables
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_NAME = os.getenv("POSTGRES_DB", "taskdb")
DB_DSN = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"

class Task(BaseModel):
    title: str
    completed: bool = False

@app.on_event("startup")
async def startup():
    try:
        app.state.pool = await asyncpg.create_pool(DB_DSN)
        async with app.state.pool.acquire() as conn:
            await conn.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL,
                    completed BOOLEAN DEFAULT FALSE
                )
            """)
    except Exception as e:
        print(f"Could not connect to DB: {e}")
        # In a real app, we might want to exit here, 
        # but for this exercise we'll let it fail gracefully in tests
        app.state.pool = None

@app.on_event("shutdown")
async def shutdown():
    if app.state.pool:
        await app.state.pool.close()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/tasks/")
async def create_task(task: Task):
    if not app.state.pool:
        raise HTTPException(status_code=500, detail="Database not connected")
    
    async with app.state.pool.acquire() as conn:
        row = await conn.fetchrow(
            "INSERT INTO tasks (title, completed) VALUES ($1, $2) RETURNING id",
            task.title, task.completed
        )
    return {"id": row["id"], **task.dict()}

@app.get("/tasks/")
async def list_tasks():
    if not app.state.pool:
        raise HTTPException(status_code=500, detail="Database not connected")

    async with app.state.pool.acquire() as conn:
        rows = await conn.fetch("SELECT id, title, completed FROM tasks")
    return [{"id": r["id"], "title": r["title"], "completed": r["completed"]} for r in rows]
