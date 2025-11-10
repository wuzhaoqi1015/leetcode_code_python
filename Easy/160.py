# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
            
        # 使用双指针法，两个指针分别遍历两个链表
        # 当某个指针到达链表末尾时，重定位到另一个链表的头部
        # 如果两个链表相交，两个指针会在相交点相遇
        # 如果不相交，两个指针最终都会到达None
        
        ptrA, ptrB = headA, headB
        
        while ptrA != ptrB:
            # 如果ptrA到达链表末尾，重定位到headB
            ptrA = ptrA.next if ptrA else headB
            # 如果ptrB到达链表末尾，重定位到headA
            ptrB = ptrB.next if ptrB else headA
            
        # 返回相交节点或None
        return ptrA
