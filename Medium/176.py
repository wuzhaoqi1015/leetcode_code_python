import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # 获取不同的薪水值
    distinct_salaries = employee['salary'].drop_duplicates()
    
    # 检查是否有至少两个不同的薪水值
    if len(distinct_salaries) < 2:
        # 如果不足两个不同的薪水值，返回None
        return pd.DataFrame({'SecondHighestSalary': [None]})
    
    # 对薪水进行降序排序并获取第二高的薪水
    sorted_salaries = distinct_salaries.sort_values(ascending=False)
    second_highest = sorted_salaries.iloc[1]
    
    # 返回包含第二高薪水的DataFrame
    return pd.DataFrame({'SecondHighestSalary': [second_highest]})
