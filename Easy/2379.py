class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_operations = float('inf')
        
        # 遍历所有长度为k的连续子串
        for i in range(n - k + 1):
            # 统计当前窗口内白色块的数量
            white_count = 0
            for j in range(i, i + k):
                if blocks[j] == 'W':
                    white_count += 1
            # 更新最小操作次数
            min_operations = min(min_operations, white_count)
        
        return min_operations
