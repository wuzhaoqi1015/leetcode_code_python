import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    # 提取所有用户ID，包括请求者和接受者
    requester = request_accepted[['requester_id']].rename(columns={'requester_id': 'id'})
    accepter = request_accepted[['accepter_id']].rename(columns={'accepter_id': 'id'})
    
    # 合并所有用户ID
    all_users = pd.concat([requester, accepter], ignore_index=True)
    
    # 计算每个用户的好友数量
    friend_count = all_users['id'].value_counts().reset_index()
    friend_count.columns = ['id', 'num']
    
    # 找到拥有最多好友的用户
    max_friends = friend_count[friend_count['num'] == friend_count['num'].max()]
    
    return max_friends
