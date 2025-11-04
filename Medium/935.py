MOD = 10**9 + 7
class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        # 定义每个数字可以跳转到的下一个数字
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        # 初始化dp数组，dp[i]表示以数字i结尾的长度为当前步数的号码数量
        dp = [1] * 10
        for _ in range(n - 1):
            new_dp = [0] * 10
            for num in range(10):
                for next_num in moves[num]:
                    new_dp[next_num] = (new_dp[next_num] + dp[num]) % MOD
            dp = new_dp
        return sum(dp) % MOD
