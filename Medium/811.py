from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # 使用字典存储每个域名的访问次数
        domain_count = {}
        
        # 遍历每个计数配对域名
        for cpdomain in cpdomains:
            # 分割计数和域名
            count_str, domain = cpdomain.split()
            count = int(count_str)
            
            # 分割域名获取所有子域名
            parts = domain.split('.')
            
            # 生成所有可能的子域名
            for i in range(len(parts)):
                # 从当前部分开始构建子域名
                subdomain = '.'.join(parts[i:])
                
                # 更新字典中的计数
                if subdomain in domain_count:
                    domain_count[subdomain] += count
                else:
                    domain_count[subdomain] = count
        
        # 构建结果列表
        result = []
        for domain, count in domain_count.items():
            result.append(f"{count} {domain}")
        
        return result
