class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 初始化公牛和奶牛计数器
        bulls = 0
        cows = 0
        
        # 使用字典记录secret和guess中非公牛数字的出现次数
        secret_count = {}
        guess_count = {}
        
        # 第一次遍历：计算公牛并记录非公牛数字
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                # 记录secret中非公牛数字
                if secret[i] in secret_count:
                    secret_count[secret[i]] += 1
                else:
                    secret_count[secret[i]] = 1
                
                # 记录guess中非公牛数字
                if guess[i] in guess_count:
                    guess_count[guess[i]] += 1
                else:
                    guess_count[guess[i]] = 1
        
        # 第二次遍历：计算奶牛
        for digit in guess_count:
            if digit in secret_count:
                # 奶牛数量取两个计数中的较小值
                cows += min(secret_count[digit], guess_count[digit])
        
        # 返回结果字符串
        return f"{bulls}A{cows}B"
