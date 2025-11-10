import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # 确保recordDate列是datetime类型
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    
    # 按日期排序，确保数据按时间顺序排列
    weather = weather.sort_values('recordDate')
    
    # 创建新列，将温度数据向后移动一天（即前一天的温度）
    weather['prev_temp'] = weather['temperature'].shift(1)
    
    # 创建新列，将日期数据向后移动一天（即前一天的日期）
    weather['prev_date'] = weather['recordDate'].shift(1)
    
    # 筛选条件：当前日期正好是前一天日期的后一天，且当前温度高于前一天温度
    result = weather[
        (weather['recordDate'] - weather['prev_date'] == pd.Timedelta(days=1)) &
        (weather['temperature'] > weather['prev_temp'])
    ]
    
    # 返回只包含id列的结果
    return result[['id']]
