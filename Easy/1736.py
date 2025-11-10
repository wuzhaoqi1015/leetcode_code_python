class Solution:
    def maximumTime(self, time: str) -> str:
        # 将字符串转换为列表便于修改
        time_list = list(time)
        
        # 处理小时部分的第一位
        if time_list[0] == '?':
            # 如果第二位是'?'或小于'4'，第一位最大可以是'2'
            if time_list[1] == '?' or int(time_list[1]) < 4:
                time_list[0] = '2'
            else:
                time_list[0] = '1'
        
        # 处理小时部分的第二位
        if time_list[1] == '?':
            # 如果第一位是'2'，第二位最大可以是'3'
            if time_list[0] == '2':
                time_list[1] = '3'
            else:
                time_list[1] = '9'
        
        # 处理分钟部分的第一位
        if time_list[3] == '?':
            time_list[3] = '5'
        
        # 处理分钟部分的第二位
        if time_list[4] == '?':
            time_list[4] = '9'
        
        # 将列表转换回字符串并返回
        return ''.join(time_list)
