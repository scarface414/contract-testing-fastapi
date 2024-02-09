from database.db import engine , Base
from database.models import Employee

#initializes the db, the table and columns are created in the DB
Base.metadata.create_all(bind = engine)