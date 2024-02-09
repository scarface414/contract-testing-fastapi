from fastapi import FastAPI
from database import db
from routes import employee

app = FastAPI()

#define the startup method

#define the middleware

app.include_router(employee.router, prefix='/api')