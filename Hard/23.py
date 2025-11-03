class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 导入堆模块
        import heapq

        # 创建最小堆
        min_heap = []
        # 创建哑节点作为结果链表的头节点
        dummy = ListNode(0)
        current = dummy

        # 遍历所有链表，将每个链表的头节点加入堆中
        for i in range(len(lists)):
            if lists[i]:
                # 堆中存储元组(val, index, node)以避免比较ListNode对象
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
                lists[i] = lists[i].next

        # 当堆不为空时循环处理
        while min_heap:
            # 弹出堆顶最小元素
            val, idx, node = heapq.heappop(min_heap)
            # 将最小节点连接到结果链表
            current.next = node
            current = current.next
            # 如果该节点所在链表还有后续节点，则将后续节点加入堆中
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))

        # 返回合并后的链表头节点
        return dummy.next
