class Solution:
    def minOperations(self, s: str) -> int:
        # 计算以'0'开头的模式需要修改的次数
        count1 = 0
        # 计算以'1'开头的模式需要修改的次数  
        count2 = 0
        
        # 遍历字符串的每个字符
        for i in range(len(s)):
            # 如果索引是偶数，应该与模式的开头字符一致
            if i % 2 == 0:
                # 以'0'开头的模式，偶数位置应该是'0'
                if s[i] != '0':
                    count1 += 1
                # 以'1'开头的模式，偶数位置应该是'1'  
                if s[i] != '1':
                    count2 += 1
            else:
                # 如果索引是奇数，应该与模式的开头字符相反
                # 以'0'开头的模式，奇数位置应该是'1'
                if s[i] != '1':
                    count1 += 1
                # 以'1'开头的模式，奇数位置应该是'0'
                if s[i] != '0':
                    count2 += 1
        
        # 返回两种模式中需要修改次数的最小值
        return min(count1, count2)
