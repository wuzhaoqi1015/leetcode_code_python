import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    # 按teacher_id分组，对每个教师的subject_id进行去重计数
    result = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    # 重命名列以符合输出要求
    result.columns = ['teacher_id', 'cnt']
    return result
