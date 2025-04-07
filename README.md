AYOMI Calculator


# RUN 

- Rquirements: Docker, Docker Compose
- Run : ```bash docker-compose up --build
- API access : http://localhost:8000
- Test API Endpoints via Swagger: http://localhost:8000/docs

# API ENDPOINTS

** POST /calculate/ ** 
* Rquest *

```json
    {
        "expression": "5 6 +"
    }
```

* Response *
```json
    {
       "expression": "5 6 +",
       "result": 11.0
    }

** GET /export/ ** 

Export all operations as CSV file

```bash
    id,expression,result
    1,"5 1 2 + 4 * + 3 -",14.0
    2,"3 4 +",7.0




