class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        # 使用快慢指针检测循环
        for i in range(n):
            # 如果当前节点已经被访问过，跳过
            if nums[i] == 0:
                continue
            
            # 初始化快慢指针
            slow = i
            fast = i
            
            # 判断方向是否一致
            def same_direction(curr, next_idx):
                # 检查当前节点和下一个节点的方向是否相同
                return nums[curr] * nums[next_idx] > 0
            
            while True:
                # 慢指针移动一步
                slow = (slow + nums[slow]) % n
                if not same_direction(i, slow):
                    break
                
                # 快指针移动两步
                fast = (fast + nums[fast]) % n
                if not same_direction(i, fast):
                    break
                fast = (fast + nums[fast]) % n
                if not same_direction(i, fast):
                    break
                
                # 如果快慢指针相遇，检测循环长度
                if slow == fast:
                    # 检查循环长度是否大于1
                    start = slow
                    curr = (start + nums[start]) % n
                    length = 1
                    while curr != start:
                        if not same_direction(start, curr):
                            length = 0
                            break
                        curr = (curr + nums[curr]) % n
                        length += 1
                    
                    if length > 1:
                        return True
                    else:
                        break
        
        return False
