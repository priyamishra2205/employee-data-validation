import pandas as pd
from .schemas import ValidationReport

def compare_datasets(source_df: pd.DataFrame, target_df: pd.DataFrame) -> list[ValidationReport]:
    """
    Compare source and target datasets to identify mismatches in department and salary.
    Returns a list of ValidationReport objects.
    """
    mismatch_reports = []

    # Merge datasets on Employee_ID for comparison
    merged_df = pd.merge(
        source_df,
        target_df,
        on="Employee_ID",
        suffixes=("_source", "_target"),
        how="outer",
        indicator=True
    )

    for _, row in merged_df.iterrows():
        employee_id = row["Employee_ID"]
        employee_name = row["Employee_Name_source"] if pd.notna(row["Employee_Name_source"]) else row["Employee_Name_target"]

        # Check for missing records
        if row["_merge"] == "left_only":
            # Record exists in source but not in target
            mismatch_reports.append(
                ValidationReport(
                    employee_id=employee_id,
                    employee_name=employee_name,
                    source_department=row["Department_source"],
                    target_department=None,
                    source_salary=row["Salary_source"],
                    target_salary=None,
                    department_mismatch=True,
                    salary_mismatch=True
                )
            )
        elif row["_merge"] == "right_only":
            # Record exists in target but not in source
            mismatch_reports.append(
                ValidationReport(
                    employee_id=employee_id,
                    employee_name=employee_name,
                    source_department=None,
                    target_department=row["Department_target"],
                    source_salary=None,
                    target_salary=row["Salary_target"],
                    department_mismatch=True,
                    salary_mismatch=True
                )
            )
        else:
            # Record exists in both datasets
            department_mismatch = row["Department_source"] != row["Department_target"]
            salary_mismatch = row["Salary_source"] != row["Salary_target"]

            if department_mismatch or salary_mismatch:
                mismatch_reports.append(
                    ValidationReport(
                        employee_id=employee_id,
                        employee_name=employee_name,
                        source_department=row["Department_source"],
                        target_department=row["Department_target"],
                        source_salary=row["Salary_source"],
                        target_salary=row["Salary_target"],
                        department_mismatch=department_mismatch,
                        salary_mismatch=salary_mismatch
                    )
                )

    return mismatch_reports

def generate_mismatch_report(source_df: pd.DataFrame, target_df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate a mismatch report as a DataFrame for CSV export.
    """
    mismatch_reports = compare_datasets(source_df, target_df)

    report_data = []
    for report in mismatch_reports:
        report_data.append(
            {
                "Employee_ID": report.employee_id,
                "Employee_Name": report.employee_name,
                "Source_Department": report.source_department,
                "Target_Department": report.target_department,
                "Source_Salary": report.source_salary,
                "Target_Salary": report.target_salary,
                "Department_Mismatch": report.department_mismatch,
                "Salary_Mismatch": report.salary_mismatch,
            }
        )

    return pd.DataFrame(report_data)