class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 使用快慢指针法检测环
        slow = nums[0]
        fast = nums[0]
        
        # 第一阶段：找到快慢指针相遇点
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # 第二阶段：找到环的入口点（重复数字）
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
