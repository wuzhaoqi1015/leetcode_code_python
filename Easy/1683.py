import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # 使用str.len()方法计算每条推文内容的长度
    # 筛选出长度严格大于15的推文
    invalid_tweets_df = tweets[tweets['content'].str.len() > 15]
    
    # 只返回tweet_id列，并确保返回DataFrame格式
    result = invalid_tweets_df[['tweet_id']]
    
    return result
