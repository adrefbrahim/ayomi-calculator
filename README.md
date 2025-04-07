AYOMI Calculator

# TOOLS / TECHNOS

-> FastAPI
-> SQLite
-> SQLAlchemy
-> Docker / Docker- Compose

# RUN 

- Rquirements: Docker, Docker Compose
- Run : ```bash docker-compose up --build```
- API access : http://localhost:8000
- Test API Endpoints via Swagger: http://localhost:8000/docs

# API ENDPOINTS

## POST /calculate/

**Request**

```json
    {
        "expression": "5 6 +"
    }
```

**Response**

```json
    {
       "expression": "5 6 +",
       "result": 11.0
    }
```
## GET /export/ 

Export all operations as CSV file

```bash
    id,expression,result
    1,"5 6 +",11.0
    2,"5 7 +",12.0
    3,"16 2 +",18.0
    4,"10 12 *",120.0 
```




