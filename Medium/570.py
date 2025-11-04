import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # 过滤出有经理的员工记录，即managerId不为空的记录
    subordinates = employee[employee['managerId'].notna()]
    
    # 按managerId分组，统计每个经理的直接下属数量
    manager_counts = subordinates.groupby('managerId').size().reset_index(name='subordinate_count')
    
    # 筛选出至少有五个直接下属的经理ID
    qualified_managers = manager_counts[manager_counts['subordinate_count'] >= 5]['managerId']
    
    # 从原始员工表中找出这些经理的姓名
    result = employee[employee['id'].isin(qualified_managers)][['name']]
    
    return result
