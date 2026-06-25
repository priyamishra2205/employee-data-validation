from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
import pandas as pd
from typing import List

from .. import schemas, validation
from ..database import get_db

router = APIRouter(prefix="/validation", tags=["validation"])

@router.post("/upload-source/", response_model=schemas.UploadResponse)
async def upload_source_data(file: UploadFile = File(...)):
    try:
        source_df = pd.read_csv(file.file)
        return {"message": "Source data uploaded successfully", "data": source_df.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error uploading source data: {str(e)}")

@router.post("/upload-target/", response_model=schemas.UploadResponse)
async def upload_target_data(file: UploadFile = File(...)):
    try:
        target_df = pd.read_csv(file.file)
        return {"message": "Target data uploaded successfully", "data": target_df.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error uploading target data: {str(e)}")

@router.post("/compare/", response_model=List[schemas.ValidationReport])
async def compare_datasets(
    source_file: UploadFile = File(...),
    target_file: UploadFile = File(...)
):
    try:
        source_df = pd.read_csv(source_file.file)
        target_df = pd.read_csv(target_file.file)
        mismatch_reports = validation.compare_datasets(source_df, target_df)
        return mismatch_reports
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error comparing datasets: {str(e)}")

@router.post("/report/", response_model=schemas.ReportResponse)
async def generate_report(
    source_file: UploadFile = File(...),
    target_file: UploadFile = File(...)
):
    try:
        source_df = pd.read_csv(source_file.file)
        target_df = pd.read_csv(target_file.file)
        report_df = validation.generate_mismatch_report(source_df, target_df)
        report_csv = report_df.to_csv(index=False)
        return {"report": report_csv}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error generating report: {str(e)}")