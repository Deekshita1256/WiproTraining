import pandas as pd

employee_data = {
    'Dept': ['IT', 'HR', 'IT', 'Sales', 'HR', 'IT', 'Sales', 'Sales'],
    'Status': ['FT', 'FT', 'Contract', 'FT', 'Contract', 'FT', 'Contract', 'FT'],
    'Salary': [95000, 60000, 70000, 80000, 55000, 98000, 72000, 85000]
}
emp_df = pd.DataFrame(employee_data)

# 1. Group by Dept and find average (mean) and maximum salary
salary_summary = emp_df.groupby('Dept')['Salary'].agg(['mean', 'max'])

# 2. Pivot Table showing employee count by Dept and Status
pivot_table = emp_df.pivot_table(index='Dept', columns='Status', aggfunc='size', fill_value=0)

# 3. Sort the pivot table by 'Contract' workers in descending order
sorted_pivot = pivot_table.sort_values(by='Contract', ascending=False)

print("Salary Summary by Dept:\n", salary_summary)
print("\nSorted Pivot Table:\n", sorted_pivot)
