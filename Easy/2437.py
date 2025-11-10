class Solution:
    def countTime(self, time: str) -> int:
        # 分离小时和分钟部分
        hh, mm = time.split(':')
        count_h = 0
        count_m = 0
        
        # 处理小时部分
        if hh[0] == '?' and hh[1] == '?':
            count_h = 24  # 00-23
        elif hh[0] == '?':
            # 根据第二位确定第一位可能的值
            if int(hh[1]) < 4:
                count_h = 3  # 第一位可以是0,1,2
            else:
                count_h = 2  # 第一位只能是0,1
        elif hh[1] == '?':
            # 根据第一位确定第二位可能的值
            if hh[0] == '2':
                count_h = 4  # 第二位可以是0,1,2,3
            else:
                count_h = 10  # 第二位可以是0-9
        else:
            count_h = 1  # 小时部分没有问号
            
        # 处理分钟部分
        if mm[0] == '?' and mm[1] == '?':
            count_m = 60  # 00-59
        elif mm[0] == '?':
            count_m = 6  # 第一位可以是0-5
        elif mm[1] == '?':
            count_m = 10  # 第二位可以是0-9
        else:
            count_m = 1  # 分钟部分没有问号
            
        return count_h * count_m
