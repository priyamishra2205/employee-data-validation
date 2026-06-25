from pydantic import BaseModel

# Schema for creating an employee
class EmployeeCreate(BaseModel):
    employee_id: int
    employee_name: str
    department: str
    salary: int

# Schema for returning an employee
class Employee(BaseModel):
    id: int
    employee_id: int
    employee_name: str
    department: str
    salary: int

    class Config:
        from_attributes = True  # Allows ORM objects to be converted to Pydantic models

# Schema for validation report
class ValidationReport(BaseModel):
    employee_id: int
    employee_name: str
    source_department: str
    target_department: str
    source_salary: int
    target_salary: int
    department_mismatch: bool
    salary_mismatch: bool

# Schema for upload response
class UploadResponse(BaseModel):
    message: str
    data: dict

# Schema for report response
class ReportResponse(BaseModel):
    report: str