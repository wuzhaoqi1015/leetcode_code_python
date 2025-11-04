class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # 使用字典存储内容到文件路径列表的映射
        content_map = {}
        
        # 遍历每个目录信息
        for path_info in paths:
            # 分割目录路径和文件信息
            parts = path_info.split()
            directory = parts[0]
            
            # 遍历每个文件信息
            for i in range(1, len(parts)):
                file_info = parts[i]
                # 找到文件名和内容的分隔位置
                left_bracket = file_info.find('(')
                right_bracket = file_info.find(')')
                
                # 提取文件名和内容
                filename = file_info[:left_bracket]
                content = file_info[left_bracket+1:right_bracket]
                
                # 构建完整文件路径
                full_path = directory + '/' + filename
                
                # 将文件路径添加到对应内容的列表中
                if content not in content_map:
                    content_map[content] = []
                content_map[content].append(full_path)
        
        # 收集所有重复文件组（至少有两个文件）
        result = []
        for paths_list in content_map.values():
            if len(paths_list) > 1:
                result.append(paths_list)
        
        return result
