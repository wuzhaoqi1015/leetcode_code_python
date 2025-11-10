class Solution:
    def canWinNim(self, n: int) -> bool:
        # 如果石头数量是4的倍数，先手必输；否则先手必胜
        return n % 4 != 0
