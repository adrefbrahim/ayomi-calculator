import io
import os 
from fastapi import FastAPI, Depends
from .compute import compute_npi
from .db_connector import get_db, Session
from .models import Operations


# Initialisation 
app = FastAPI()


@app.post('/compute/')
def compute(expression: str, db: Session = Depends(get_db)):
    response = dict()
    
    result = compute_npi(expression)
    operation = Operations(expression=expression, result=str(result))
    db.add(operation)
    db.commit()
    
    response['expression'] = expression
    response['result'] = result
    return  response