class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        # 遍历所有可能的起始位置
        for i in range(n - m * k + 1):
            found = True
            # 检查后续k-1个模式段是否与第一个模式段匹配
            for j in range(1, k):
                # 检查每个模式段中的每个元素
                for l in range(m):
                    if i + l + j * m >= n or arr[i + l] != arr[i + l + j * m]:
                        found = False
                        break
                if not found:
                    break
            if found:
                return True
        return False
