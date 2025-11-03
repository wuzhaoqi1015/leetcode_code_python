class Solution:
    def numTrees(self, n: int) -> int:
        # 使用动态规划，dp[i]表示i个节点能组成的二叉搜索树数量
        dp = [0] * (n + 1)
        # 空树和只有一个节点的情况都只有1种
        dp[0] = 1
        dp[1] = 1
        
        # 计算从2到n个节点的情况
        for i in range(2, n + 1):
            # 对于i个节点，遍历每个节点作为根节点的情况
            for j in range(1, i + 1):
                # 左子树有j-1个节点，右子树有i-j个节点
                # 左右子树组合数相乘即为以j为根节点的BST数量
                dp[i] += dp[j - 1] * dp[i - j]
        
        return dp[n]
