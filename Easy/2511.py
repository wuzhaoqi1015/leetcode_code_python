class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        max_capture = 0
        
        # 遍历所有可能的起点（我方城堡）
        for i in range(n):
            if forts[i] == 1:  # 找到我方城堡
                # 向左搜索
                j = i - 1
                count = 0
                while j >= 0:
                    if forts[j] == 0:  # 遇到敌人城堡，计数
                        count += 1
                    elif forts[j] == 1:  # 遇到我方城堡，中断
                        break
                    else:  # 遇到空位置，更新最大值并中断
                        if count > 0:
                            max_capture = max(max_capture, count)
                        break
                    j -= 1
                
                # 向右搜索
                j = i + 1
                count = 0
                while j < n:
                    if forts[j] == 0:  # 遇到敌人城堡，计数
                        count += 1
                    elif forts[j] == 1:  # 遇到我方城堡，中断
                        break
                    else:  # 遇到空位置，更新最大值并中断
                        if count > 0:
                            max_capture = max(max_capture, count)
                        break
                    j += 1
        
        return max_capture
