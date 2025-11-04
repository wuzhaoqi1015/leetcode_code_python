import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # 按分数降序排序
    scores_sorted = scores.sort_values(by='score', ascending=False)
    
    # 使用rank方法计算密集排名，method='dense'确保排名连续无空缺
    scores_sorted['rank'] = scores_sorted['score'].rank(method='dense', ascending=False).astype(int)
    
    # 选择需要的列并返回结果
    result = scores_sorted[['score', 'rank']]
    
    return result
