from sqlalchemy import Column, Integer, String
from .database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, unique=True, index=True)
    employee_name = Column(String(100))
    department = Column(String(50))
    salary = Column(Integer)