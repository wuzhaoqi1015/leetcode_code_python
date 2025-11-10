class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()  # 使用集合存储唯一的电子邮件地址
        
        for email in emails:
            # 分割本地名和域名
            local_name, domain = email.split('@')
            
            # 处理本地名：移除第一个加号之后的所有内容
            if '+' in local_name:
                local_name = local_name.split('+')[0]
            
            # 处理本地名：移除所有的点号
            local_name = local_name.replace('.', '')
            
            # 重新组合成标准化的电子邮件地址
            normalized_email = local_name + '@' + domain
            
            # 添加到集合中（自动去重）
            unique_emails.add(normalized_email)
        
        # 返回唯一地址的数量
        return len(unique_emails)
