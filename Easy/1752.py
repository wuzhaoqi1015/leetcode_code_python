class Solution:
    def check(self, nums: List[int]) -> bool:
        # 找到可能的旋转点
        n = len(nums)
        count = 0
        
        # 遍历数组，检查相邻元素的大小关系
        for i in range(n):
            # 如果当前元素大于下一个元素（考虑循环），则可能是一个旋转点
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                # 如果找到超过一个旋转点，说明无法通过旋转得到
                if count > 1:
                    return False
        
        # 最多只能有一个旋转点
        return count <= 1
