class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        # 使用两个变量记录当前上升和下降摆动序列的长度
        up = 1
        down = 1
        
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                # 当前数字比前一个大，可以接在下降摆动序列后面形成更长的上升摆动序列
                up = down + 1
            elif nums[i] < nums[i-1]:
                # 当前数字比前一个小，可以接在上升摆动序列后面形成更长的下降摆动序列
                down = up + 1
        
        # 返回上升和下降摆动序列中的较大值
        return max(up, down)
