import io
import os 
import csv
from fastapi import FastAPI, Depends
from fastapi.responses import StreamingResponse
from .compute import compute_npi
from .db_connector import get_db, Session
from .models import Operations
from .util import push_to_db, prepare_export

# Initialisation 
app = FastAPI()


@app.post('/compute/')
def compute(expression: str, db: Session = Depends(get_db)):
    response = dict()
    result = compute_npi(expression)
    response['expression'] = expression
    response['result'] = result
    push_to_db(db, response)
    return  response

@app.get('/export/')
def export_all(db: Session = Depends(get_db)):
    output = prepare_export(db)
    return StreamingResponse(output, media_type='text/csv', headers={"Content-Disposition": "attachment; filename=calculations.csv"})