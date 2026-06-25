from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, crud
from ..database import get_db

router = APIRouter(prefix="/employees", tags=["employees"])

# Create an employee
@router.post("/", response_model=schemas.Employee)
def create_employee_endpoint(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)

# Get all employees
@router.get("/", response_model=List[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = crud.get_employees(db, skip=skip, limit=limit)
    return employees

# Get an employee by ID
@router.get("/{employee_id}", response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

# Update an employee
@router.put("/{employee_id}", response_model=schemas.Employee)
def update_employee_endpoint(employee_id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.update_employee(db=db, employee_id=employee_id, employee=employee)

# Delete an employee
@router.delete("/{employee_id}", response_model=schemas.Employee)
def delete_employee_endpoint(employee_id: int, db: Session = Depends(get_db)):
    return crud.delete_employee(db=db, employee_id=employee_id)