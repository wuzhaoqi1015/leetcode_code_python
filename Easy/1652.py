class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        
        if k == 0:
            return result
        
        # 处理k为正数的情况
        if k > 0:
            for i in range(n):
                total = 0
                # 计算接下来k个数字的和
                for j in range(1, k + 1):
                    total += code[(i + j) % n]
                result[i] = total
        # 处理k为负数的情况
        else:
            k = abs(k)  # 取绝对值
            for i in range(n):
                total = 0
                # 计算之前k个数字的和
                for j in range(1, k + 1):
                    total += code[(i - j) % n]
                result[i] = total
        
        return result
