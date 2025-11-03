class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 使用回溯法来寻找所有可能的分割方案
        def backtrack(start, path):
            # 如果起始位置已经到达字符串末尾，说明找到了一种分割方案
            if start == len(s):
                result.append(path[:])  # 添加当前路径的副本到结果中
                return
            # 从起始位置开始尝试所有可能的分割点
            for end in range(start + 1, len(s) + 1):
                # 检查从start到end-1的子串是否是回文
                substring = s[start:end]
                if substring == substring[::-1]:  # 通过反转字符串判断回文
                    path.append(substring)  # 如果是回文，添加到当前路径
                    backtrack(end, path)    # 递归处理剩余部分
                    path.pop()              # 回溯，移除最后添加的子串
        
        result = []  # 存储所有可能的分割方案
        backtrack(0, [])  # 从字符串的起始位置开始回溯
        return result
