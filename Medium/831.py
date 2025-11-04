class Solution:
    def maskPII(self, s: str) -> str:
        # 检查是否为邮箱地址
        if '@' in s:
            # 将整个字符串转换为小写
            s = s.lower()
            # 分割用户名和域名
            name, domain = s.split('@')
            # 处理用户名：保留首尾字符，中间用5个星号替换
            masked_name = name[0] + '*****' + name[-1]
            # 返回隐藏后的邮箱
            return masked_name + '@' + domain
        else:
            # 处理电话号码：移除所有分隔符
            digits = ''.join(c for c in s if c.isdigit())
            # 获取本地号码的最后4位
            last_four = digits[-4:]
            # 根据国家代码长度确定格式
            country_code_len = len(digits) - 10
            if country_code_len == 0:
                return "***-***-" + last_four
            elif country_code_len == 1:
                return "+*-***-***-" + last_four
            elif country_code_len == 2:
                return "+**-***-***-" + last_four
            else:
                return "+***-***-***-" + last_four
