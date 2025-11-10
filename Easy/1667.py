import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # 使用str.capitalize()方法将每个名字的首字母大写，其余字母小写
    users['name'] = users['name'].str.capitalize()
    # 按user_id排序结果表
    result = users.sort_values('user_id')
    return result
