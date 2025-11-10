class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # 统计奇数位置和偶数位置的筹码数量
        odd_count = 0
        even_count = 0
        
        # 遍历所有筹码位置
        for pos in position:
            if pos % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        # 最小代价是将数量较少的那部分筹码移动到数量较多的位置
        # 因为移动2步代价为0，所以奇数位置和偶数位置之间可以自由移动
        # 只需要考虑将奇数位置和偶数位置统一到一个位置的最小代价
        return min(odd_count, even_count)
