class Solution:
    def grayCode(self, n: int) -> List[int]:
        # 使用镜像反射法生成格雷码序列
        res = [0]  # 初始化结果列表，包含起始值0
        for i in range(n):
            # 每次迭代将当前结果镜像后加上2^i
            head = 1 << i  # 计算当前最高位的值
            # 倒序遍历当前结果，为每个元素加上head后追加到结果列表
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] | head)
        return res
