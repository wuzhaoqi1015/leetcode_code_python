class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # 计算单个数字的权重（步数）
        def get_weight(num):
            steps = 0
            while num != 1:
                if num % 2 == 0:
                    num = num // 2
                else:
                    num = 3 * num + 1
                steps += 1
            return steps
        
        # 生成区间内所有数字及其权重
        nums_with_weights = []
        for num in range(lo, hi + 1):
            weight = get_weight(num)
            nums_with_weights.append((weight, num))
        
        # 按权重升序排序，权重相同则按数字升序
        nums_with_weights.sort(key=lambda x: (x[0], x[1]))
        
        # 返回第k个数字（k从1开始）
        return nums_with_weights[k-1][1]
