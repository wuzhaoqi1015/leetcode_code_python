class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # 获取字符串数组的长度和每个字符串的长度
        n = len(strs)
        m = len(strs[0])
        
        # 初始化要删除的列数
        delete_count = 0
        
        # 遍历每一列
        for col in range(m):
            # 检查当前列是否不是非严格递增
            for row in range(1, n):
                # 如果当前行的字符小于前一行的字符，说明不是非严格递增
                if strs[row][col] < strs[row-1][col]:
                    delete_count += 1
                    break  # 发现一个不符合的列就跳出内层循环
        
        return delete_count
