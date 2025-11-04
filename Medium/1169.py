class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # 解析每笔交易，存储为元组列表
        parsed = []
        for i, trans in enumerate(transactions):
            name, time, amount, city = trans.split(',')
            parsed.append((name, int(time), int(amount), city, i))
        
        # 按交易时间排序以便比较
        parsed.sort(key=lambda x: x[1])
        
        invalid_indices = set()
        n = len(parsed)
        
        # 检查每笔交易是否无效
        for i in range(n):
            name1, time1, amount1, city1, idx1 = parsed[i]
            
            # 检查金额是否超过1000
            if amount1 > 1000:
                invalid_indices.add(idx1)
                continue
            
            # 检查与同名不同城市的交易是否在60分钟内
            for j in range(n):
                if i == j:
                    continue
                    
                name2, time2, amount2, city2, idx2 = parsed[j]
                
                # 如果名称相同且城市不同
                if name1 == name2 and city1 != city2:
                    # 检查时间差是否在60分钟内
                    if abs(time1 - time2) <= 60:
                        invalid_indices.add(idx1)
                        invalid_indices.add(idx2)
        
        # 根据索引收集无效交易
        result = []
        for idx in invalid_indices:
            result.append(transactions[idx])
        
        return result
