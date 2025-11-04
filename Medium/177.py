import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # 获取不同的工资值并降序排列
    distinct_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # 检查是否有足够的不同的工资值
    if len(distinct_salaries) < N or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # 获取第N高的工资
    nth_highest = distinct_salaries.iloc[N-1]
    
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest]})
