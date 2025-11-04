# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 由于无法访问head，且node不是最后一个节点
        # 将下一个节点的值复制到当前节点，然后删除下一个节点
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
        # 断开与下一个节点的连接
        next_node.next = None
