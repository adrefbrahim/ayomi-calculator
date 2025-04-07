import io
import os 
import csv
from fastapi import FastAPI, Depends
from fastapi.responses import StreamingResponse
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

@app.get('/export/')
def export_all(db: Session = Depends(get_db)):
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['id', 'expression', 'result'])
    operations = db.query(Operations).all()

    for op in operations:
        writer.writerow([op.id, op.expression, op.result])
    
    output.seek(0)
    return StreamingResponse(output, media_type='text/csv', headers={"Content-Disposition": "attachment; filename=calculations.csv"})