# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        # 将nums转换为集合，提高查找效率
        num_set = set(nums)
        count = 0
        current = head
        in_component = False  # 标记当前是否在组件中
        
        while current:
            if current.val in num_set:
                # 如果当前节点在nums中，且不在组件中，说明是新组件的开始
                if not in_component:
                    count += 1
                    in_component = True
            else:
                # 当前节点不在nums中，标记不在组件中
                in_component = False
            current = current.next
        
        return count
