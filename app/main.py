from fastapi import FastAPI
from .database import engine, Base
from .routes import employee, validation_api

# Create the database tables
def create_tables():
    Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI(
    title="Employee Data Validation System",
    description="A system to validate employee data between source and target datasets.",
    version="1.0.0",
)

# Include routers
app.include_router(employee.router)
app.include_router(validation_api.router)

# Create tables on startup
@app.on_event("startup")
def on_startup():
    create_tables()
    