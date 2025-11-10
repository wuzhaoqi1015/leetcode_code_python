import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # 生成所有学生和所有科目的笛卡尔积
    all_combinations = students.merge(subjects, how='cross')
    
    # 计算每个学生参加每个科目考试的次数
    exam_counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    
    # 将考试次数与所有组合进行左连接，缺失值填充为0
    result = all_combinations.merge(exam_counts, on=['student_id', 'subject_name'], how='left')
    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)
    
    # 按student_id和subject_name排序
    result = result.sort_values(['student_id', 'subject_name']).reset_index(drop=True)
    
    return result
