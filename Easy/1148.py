import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # 筛选出作者浏览自己文章的记录（author_id等于viewer_id）
    result_df = views[views['author_id'] == views['viewer_id']]
    
    # 提取唯一的作者ID并转换为DataFrame
    unique_authors = result_df['author_id'].unique()
    
    # 创建结果DataFrame，列名为'id'
    result = pd.DataFrame({'id': unique_authors})
    
    # 按id升序排序
    result = result.sort_values(by='id')
    
    # 重置索引（保持输出格式整洁）
    result = result.reset_index(drop=True)
    
    return result
