from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/", summary='Get a hello world json')
def get_root(name:str = 'World!',):
    """
    Hello World!
    1. processes requests
    1. return greeting
    """
    return {"Hello": name}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}