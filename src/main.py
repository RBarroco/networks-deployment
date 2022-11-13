from fastapi import FastAPI, Query, HTTPException
import pandas
from pydantic import BaseModel
from src.model import predict, converts

app = FastAPI()

# uvicorn src.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
@app.get("/ping")
def pong():
    return {"ping": "pong!"}

# pydantic models should we input dict
class Input(BaseModel):
    input: dict

class Output(Input):
    forecast: int

@app.post("/predict", response_model=Output, status_code=200)
def get_prediction(payload: Input):
    input = payload.input

    output = predict(input)

    if not output:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {
        "input": input, 
        "output": converts(output)}
    return response_object


#     {'Unnamed: 0': 0,
#   'Received Packets': 132,
#   'Received Bytes': 9181,
#   'Sent Bytes': 6311853,
#   'Sent Packets': 238,
#   'Port alive Duration (S)': 46,
#   'Delta Received Packets': 0,
#   'Delta Received Bytes': 0,
#   'Delta Sent Bytes': 280,
#   'Delta Sent Packets': 2,
#   'Delta Port alive Duration (S)': 5,
#   'Connection Point': 1,
#   'Total Load/Rate': 0,
#   'Total Load/Latest': 0,
#   'Active Flow Entries': 9,
#   'Switch ID_of:0000000000000002': 0,
#   'Switch ID_of:0000000000000003': 0,
#   'Switch ID_of:0000000000000004': 0,
#   'Switch ID_of:0000000000000005': 0,
#   'Switch ID_of:0000000000000006': 0,
#   'Switch ID_of:0000000000000007': 0,
#   'Switch ID_of:0000000000000008': 0,
#   'Switch ID_of:0000000000000009': 0,
#   'Switch ID_of:000000000000000a': 0,
#   'Switch ID_of:000000000000000b': 0,
#   'Switch ID_of:000000000000000c': 1,
#   'Port Number_Port#:2': 0,
#   'Port Number_Port#:3': 0,
#   'Port Number_Port#:4': 0}