from typing import Optional

from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class EmployeeModel(BaseModel):
    id : Optional[int] = 1
    name : str = Field(min_length=3, max_length=25)
    department : str = Field(min_length=3, max_length=25)
    age : int = Field(ge = '18' , le = '60')
    created_at : Optional[datetime] = None
    updated_at : Optional[datetime] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name" : "Nishith Baravkar" , 
                    "department" : "CSE" , 
                    "age" : 21 
                }
            ]
        }
    }