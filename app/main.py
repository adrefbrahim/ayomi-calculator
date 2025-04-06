import io
import os 
from fastapi import FastAPI
from .compute import compute_npi


# Initialisation 
app = FastAPI()


@app.post('/compute/')
def compute(expression: str):
    response = dict()
    response['expression'] = expression
    response['result'] = compute_npi(expression)
    return  response