# Module of utils functions
import io
import csv
from .models import Operations

def push_to_db(db, response):
    operation = Operations(expression=response['expression'], result=str(response['result']))
    db.add(operation)
    db.commit()

def prepare_export(db):
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['id', 'expression', 'result'])
    operations = db.query(Operations).all()

    for op in operations:
        writer.writerow([op.id, op.expression, op.result])
    output.seek(0)
    return output