from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

@app.get("/data/message1")
def get_message1():
    return {"message": "Endpoint 1 - Hello, world!"}

@app.get("/data/message2")
def get_message2():
    return {"message": "Endpoint 2 - Hello, world!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
