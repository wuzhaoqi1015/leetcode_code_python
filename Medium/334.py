class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # 初始化两个变量，分别记录当前遇到的最小值和次小值
        first = float('inf')
        second = float('inf')
        
        # 遍历数组中的每个元素
        for num in nums:
            # 如果当前元素小于等于first，更新first
            if num <= first:
                first = num
            # 如果当前元素大于first但小于等于second，更新second
            elif num <= second:
                second = num
            # 如果当前元素大于second，说明找到了递增三元组
            else:
                return True
                
        # 遍历结束仍未找到符合条件的递增三元组
        return False
