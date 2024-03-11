# main.py file

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"greeting": "Hi there!"}
