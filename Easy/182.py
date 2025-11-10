import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # 使用groupby对email进行分组，计算每组的数量
    email_counts = person.groupby('email').size().reset_index(name='count')
    
    # 筛选出出现次数大于1的email
    duplicate_emails_df = email_counts[email_counts['count'] > 1][['email']]
    
    # 重命名列名为Email
    duplicate_emails_df.columns = ['Email']
    
    return duplicate_emails_df
