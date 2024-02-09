from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Path, status, Query
from fastapi.encoders import jsonable_encoder

from database.db import Session , engine

from schemas import EmployeeModel
from database.models import Employee

session = Session(bind=engine)

router = APIRouter(prefix="/employees", tags=["SetDefault"])


@router.get("/" , response_model=List[EmployeeModel])
async def get_all_employees() : 
    employee_list = session.query(Employee).order_by("id").all()
    return employee_list
    

@router.post("/" , response_model= EmployeeModel , status_code=status.HTTP_201_CREATED)
async def create_employee(body: EmployeeModel) : 
    
    new_employee = Employee(
        name = body.name , 
        age = body.age ,
        department= body.department
    )
    session.add(new_employee)
    session.commit()

    return new_employee


@router.get("/{userid}")
async def get_employee_by_ID(userid : int) : 
    user = session.query(Employee).filter(Employee.id == userid).first()

    if user is None : 
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user does not exist")

    return user

@router.put("/update/{userid}")
async def update_employee_by_ID(userid : int , body : EmployeeModel) : 
    user = session.query(Employee).filter(Employee.id == userid).first()

    if user is None : 
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user does not exist")

    user.name = body.name 
    user.age = body.age 
    user.department = body.department

    session.commit()

    user = session.query(Employee).filter(Employee.id == userid).first()
    return user