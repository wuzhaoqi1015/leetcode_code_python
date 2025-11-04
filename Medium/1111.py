class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        # 初始化结果列表和当前深度
        res = []
        depth = 0
        
        # 遍历输入字符串中的每个字符
        for c in seq:
            if c == '(':
                # 遇到左括号时深度加1
                depth += 1
                # 根据当前深度的奇偶性分配分组
                res.append(depth % 2)
            else:
                # 遇到右括号时根据当前深度的奇偶性分配分组
                res.append(depth % 2)
                # 然后深度减1
                depth -= 1
        
        return res
