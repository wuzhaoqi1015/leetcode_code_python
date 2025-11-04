class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # 按照每个数对的第二个元素进行升序排序
        pairs.sort(key=lambda x: x[1])
        
        # 初始化当前链的末尾值和链长度
        current_end = -float('inf')
        chain_length = 0
        
        # 遍历排序后的数对
        for pair in pairs:
            # 如果当前数对的第一个元素大于当前链的末尾值
            if pair[0] > current_end:
                # 更新链的末尾值为当前数对的第二个元素
                current_end = pair[1]
                # 链长度加1
                chain_length += 1
                
        return chain_length
