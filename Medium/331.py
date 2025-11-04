class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # 使用槽位概念来验证前序序列
        # 初始时有一个槽位用于根节点
        slots = 1
        nodes = preorder.split(',')
        
        for node in nodes:
            # 处理每个节点前，消耗一个槽位
            slots -= 1
            
            # 如果槽位变为负数，说明序列无效
            if slots < 0:
                return False
            
            # 如果当前节点不是空节点，则增加两个槽位（左右子节点）
            if node != '#':
                slots += 2
        
        # 最终槽位应该正好为0才表示序列有效
        return slots == 0
