import pandas as pd
 
source_df = pd.DataFrame({
    "Employee_ID": range(1, 16),
    "Employee_Name": [
        "Emp1", "Emp2", "Emp3", "Emp4", "Emp5",
        "Emp6", "Emp7", "Emp8", "Emp9", "Emp10",
        "Emp11", "Emp12", "Emp13", "Emp14", "Emp15"
    ],
    "Department": [
        "IT", "HR", "Finance", "IT", "Admin",
        "HR", "IT", "Finance", "Admin", "HR",
        "IT", "Finance", "Admin", "HR", "IT"
    ],
    "Salary": [
        50000, 45000, 60000, 55000, 40000,
        47000, 52000, 61000, 42000, 48000,
        53000, 62000, 43000, 49000, 54000
    ]
})
 
print(source_df)
#Target DataFrame (15 Records with Mismatches)
target_df = pd.DataFrame({
    "Employee_ID": range(1, 16),
    "Employee_Name": [
        "Emp1", "Emp2", "Emp3", "Emp4", "Emp5",
        "Emp6", "Emp7", "Emp8", "Emp9", "Emp10",
        "Emp11", "Emp12", "Emp13", "Emp14", "Emp15"
    ],
    "Department": [
        "IT", "HR", "Finance", "IT", "Admin",
        "HR", "IT", "Finance", "Admin", "HR",
        "IT", "Finance", "Sales", "HR", "IT"   # Mismatch
    ],
    "Salary": [
        50000, 45000, 65000, 55000, 40000,      # Salary mismatch
        47000, 52000, 61000, 42000, 48000,
        53000, 62000, 43000, 49000, 56000       # Salary mismatch
    ]
})
 
print(target_df)
import os

# Get absolute path to the 'data' directory
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.abspath(os.path.join(current_dir, "..", "data"))

source_df.to_csv(os.path.join(data_dir, "source.csv"), index=False)
target_df.to_csv(os.path.join(data_dir, "target.csv"), index=False)
