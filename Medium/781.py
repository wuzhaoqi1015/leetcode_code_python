class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        from collections import Counter
        
        # 统计每种回答出现的次数
        count_dict = Counter(answers)
        total = 0
        
        # 遍历每种回答值
        for key, value in count_dict.items():
            # 如果回答为0，表示没有其他同色兔子，每只单独计算
            if key == 0:
                total += value
            else:
                # 计算每组同色兔子的数量（key + 1）
                group_size = key + 1
                # 计算需要多少组才能容纳所有给出该回答的兔子
                groups = (value + group_size - 1) // group_size
                total += groups * group_size
        
        return total
