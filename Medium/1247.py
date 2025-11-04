class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # 统计不匹配位置的字符对
        xy_count = 0
        yx_count = 0
        
        # 遍历字符串，统计不匹配的字符对
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x' and s2[i] == 'y':
                    xy_count += 1
                else:
                    yx_count += 1
        
        # 检查总数是否为偶数，因为每次交换需要处理两个位置
        # 如果总数是奇数，则无法完成匹配
        if (xy_count + yx_count) % 2 != 0:
            return -1
        
        # 计算最小交换次数
        # 对于xy和yx对，有两种交换方式：
        # 1. 两个xy对或两个yx对可以通过一次交换解决
        # 2. 一个xy对和一个yx对需要两次交换
        result = xy_count // 2 + yx_count // 2
        if xy_count % 2 == 1:
            result += 2
        
        return result
