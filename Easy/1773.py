class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # 定义规则键对应的索引位置
        rule_map = {"type": 0, "color": 1, "name": 2}
        # 获取当前规则对应的索引
        idx = rule_map[ruleKey]
        count = 0
        # 遍历所有物品
        for item in items:
            # 检查当前物品在规则索引位置的值是否匹配规则值
            if item[idx] == ruleValue:
                count += 1
        return count
