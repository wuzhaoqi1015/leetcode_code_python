class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # 将数组按降序排序，便于从最大的边开始检查
        nums.sort(reverse=True)
        
        # 遍历数组，检查连续的三个元素是否能构成三角形
        for i in range(len(nums) - 2):
            # 三角形条件：任意两边之和大于第三边
            # 由于数组已排序，只需检查两个较小边之和是否大于最大边
            if nums[i] < nums[i+1] + nums[i+2]:
                # 满足条件，返回这三条边的周长
                return nums[i] + nums[i+1] + nums[i+2]
        
        # 遍历完都没有找到能构成三角形的三条边，返回0
        return 0
