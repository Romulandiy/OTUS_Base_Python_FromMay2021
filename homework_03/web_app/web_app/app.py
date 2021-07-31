from fastapi import FastAPI

app = FastAPI()


@app.get("/", summary='Get a hello world json')
def read_root():
    return {"Hello": "World 3234424"}
