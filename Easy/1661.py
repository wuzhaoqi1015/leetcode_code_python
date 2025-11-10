import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    # 将数据按machine_id和process_id分组，分别提取start和end时间戳
    start_df = activity[activity['activity_type'] == 'start'][['machine_id', 'process_id', 'timestamp']]
    end_df = activity[activity['activity_type'] == 'end'][['machine_id', 'process_id', 'timestamp']]
    
    # 合并start和end数据，计算每个进程的耗时
    merged_df = pd.merge(start_df, end_df, on=['machine_id', 'process_id'], suffixes=('_start', '_end'))
    merged_df['process_time'] = merged_df['timestamp_end'] - merged_df['timestamp_start']
    
    # 按机器分组计算平均耗时
    result_df = merged_df.groupby('machine_id')['process_time'].mean().reset_index()
    result_df['processing_time'] = result_df['process_time'].round(3)
    
    # 返回最终结果，只保留需要的列
    return result_df[['machine_id', 'processing_time']]
