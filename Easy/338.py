class Solution:
    def countBits(self, n: int) -> List[int]:
        # 初始化结果数组，长度为n+1，初始值全为0
        ans = [0] * (n + 1)
        
        # 使用动态规划方法，利用已知结果计算后续数字的1的个数
        # 对于每个数字i，其1的个数等于i右移一位的数字的1的个数加上i的最低位是否为1
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        
        return ans
