from fastapi import FastAPI, Query, HTTPException
import pandas
from pydantic import BaseModel
from src.model import predict, converts

app = FastAPI()

# uvicorn src.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
@app.get("/ping")
def pong():
    return {"ping": "pong!"}

# pydantic models
class Input(BaseModel):
    input: str

class Output(Input):
    forecast: int

@app.post("/predict", response_model=Output, status_code=200)
def get_prediction(payload: Input):
    input = payload.input

    output = predict(input[:1])

    if not output:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {
        "input": input[:1], 
        "output": converts(output)}
    return response_object