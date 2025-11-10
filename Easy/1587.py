import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    # 计算每个账户的交易总额
    account_balance = transactions.groupby('account')['amount'].sum().reset_index()
    account_balance.rename(columns={'amount': 'balance'}, inplace=True)
    
    # 合并用户表和余额表
    result = pd.merge(users, account_balance, on='account', how='inner')
    
    # 筛选余额大于10000的用户
    result = result[result['balance'] > 10000]
    
    # 选择需要的列并重命名
    result = result[['name', 'balance']]
    
    return result
