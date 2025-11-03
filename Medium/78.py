class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        
        # 使用位运算生成所有子集
        # 总共有2^n个子集，每个子集对应一个二进制位掩码
        for i in range(1 << n):
            subset = []
            # 检查每个位是否被设置
            for j in range(n):
                # 如果第j位为1，则将对应元素加入子集
                if i & (1 << j):
                    subset.append(nums[j])
            result.append(subset)
        
        return result
