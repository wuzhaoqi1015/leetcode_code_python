class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # 将版本号字符串按点分割成修订号列表
        v1_list = version1.split('.')
        v2_list = version2.split('.')
        
        # 获取两个版本号的最大修订号数量
        max_length = max(len(v1_list), len(v2_list))
        
        # 逐个比较修订号
        for i in range(max_length):
            # 获取当前修订号，如果超出范围则设为0
            v1_num = int(v1_list[i]) if i < len(v1_list) else 0
            v2_num = int(v2_list[i]) if i < len(v2_list) else 0
            
            # 比较当前修订号
            if v1_num < v2_num:
                return -1
            elif v1_num > v2_num:
                return 1
        
        # 所有修订号都相等
        return 0
