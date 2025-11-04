from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 建立邮箱到账户索引的映射
        email_to_index = {}
        # 并查集数组
        parent = list(range(len(accounts)))
        
        # 查找根节点
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # 合并两个集合
        def union(x: int, y: int):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_y] = root_x
        
        # 遍历所有账户，建立邮箱到索引的映射并合并有相同邮箱的账户
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_index:
                    # 如果邮箱已存在，合并当前账户和之前记录该邮箱的账户
                    union(email_to_index[email], i)
                else:
                    email_to_index[email] = i
        
        # 将每个账户的邮箱合并到其根账户
        merged_accounts = {}
        for i, account in enumerate(accounts):
            root = find(i)
            if root not in merged_accounts:
                merged_accounts[root] = set()
            # 添加当前账户的所有邮箱到对应根账户的集合中
            merged_accounts[root].update(account[1:])
        
        # 构建结果列表
        result = []
        for root, emails in merged_accounts.items():
            # 获取账户名称
            name = accounts[root][0]
            # 将邮箱排序并按格式添加到结果中
            sorted_emails = sorted(emails)
            result.append([name] + sorted_emails)
        
        return result
