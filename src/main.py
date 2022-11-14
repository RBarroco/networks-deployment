from fastapi import FastAPI, Query, HTTPException
import pandas as pd
from pydantic import BaseModel
from typing import Dict
from model import predict

app = FastAPI()

# uvicorn src.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
@app.get("/ping")
def pong():
    return {"ping": "pong!"}

# pydantic models should we input dict
class Input(BaseModel):
    input: str

class Output(BaseModel):
    forecast: str

@app.post("/predict", response_model=Output, status_code=200)
def get_prediction(payload: Input):
    input = payload.input

    output = predict(input)

    if not output:
        raise HTTPException(status_code=400, detail="Model not found.")

    return output


# @app.post("/predict", response_model=Output, status_code=200)
# def get_prediction(payload: Input):
#     input = pd.DataFrame.read_json(payload.input)

#     output = predict(input)

#     if not output:
#         raise HTTPException(status_code=400, detail="Model not found.")

#     return output
