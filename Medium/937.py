class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 分离字母日志和数字日志
        letter_logs = []
        digit_logs = []
        
        for log in logs:
            # 找到第一个空格后的内容
            content = log.split(' ', 1)[1]
            # 判断是字母日志还是数字日志
            if content[0].isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)
        
        # 对字母日志进行排序
        # 排序规则：先按内容排序，内容相同按标识符排序
        letter_logs.sort(key=lambda x: (x.split(' ', 1)[1], x.split(' ', 1)[0]))
        
        # 合并结果：字母日志在前，数字日志在后
        return letter_logs + digit_logs
