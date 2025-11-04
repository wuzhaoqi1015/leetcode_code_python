import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    # 第一部分：查找评论电影数量最多的用户名
    # 按用户ID分组统计评论数量
    user_review_counts = movie_rating.groupby('user_id').size().reset_index(name='review_count')
    # 合并用户表获取用户名
    user_reviews = user_review_counts.merge(users, on='user_id', how='inner')
    # 按评论数量降序、用户名升序排序
    user_reviews_sorted = user_reviews.sort_values(['review_count', 'name'], ascending=[False, True])
    # 获取第一个结果（评论数量最多且字典序最小的用户名）
    top_user = user_reviews_sorted.iloc[0]['name']
    
    # 第二部分：查找2020年2月平均评分最高的电影名称
    # 过滤2020年2月的评分记录
    movie_rating['created_at'] = pd.to_datetime(movie_rating['created_at'])
    feb_2020_ratings = movie_rating[
        (movie_rating['created_at'].dt.year == 2020) & 
        (movie_rating['created_at'].dt.month == 2)
    ]
    # 按电影ID分组计算平均评分
    movie_avg_ratings = feb_2020_ratings.groupby('movie_id')['rating'].mean().reset_index(name='avg_rating')
    # 合并电影表获取电影名称
    movie_ratings_with_title = movie_avg_ratings.merge(movies, on='movie_id', how='inner')
    # 按平均评分降序、电影名称升序排序
    movie_ratings_sorted = movie_ratings_with_title.sort_values(['avg_rating', 'title'], ascending=[False, True])
    # 获取第一个结果（平均评分最高且字典序最小的电影名称）
    top_movie = movie_ratings_sorted.iloc[0]['title']
    
    # 创建结果DataFrame
    result_df = pd.DataFrame({
        'results': [top_user, top_movie]
    })
    
    return result_df
