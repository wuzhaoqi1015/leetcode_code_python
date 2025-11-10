class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 对孩子的胃口值和饼干尺寸进行排序
        g.sort()
        s.sort()
        
        # 初始化指针和计数器
        child_ptr = 0
        cookie_ptr = 0
        satisfied_children = 0
        
        # 使用贪心算法分配饼干
        while child_ptr < len(g) and cookie_ptr < len(s):
            # 如果当前饼干能满足当前孩子的胃口
            if s[cookie_ptr] >= g[child_ptr]:
                satisfied_children += 1  # 满足一个孩子
                child_ptr += 1           # 移动到下一个孩子
            cookie_ptr += 1              # 无论是否满足，都尝试下一块饼干
        
        return satisfied_children
