class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 递归函数，通过父行的位置和值来确定当前字符
        def find_kth(row, pos, current_val):
            # 如果到达第一行，直接返回当前值
            if row == 1:
                return current_val
            # 计算当前行长度的一半
            half = 2 ** (row - 2)
            # 如果位置在前半部分，递归到上一行的对应位置
            if pos <= half:
                return find_kth(row - 1, pos, current_val)
            else:
                # 如果在后半部分，根据当前值决定递归的值：0 -> 1, 1 -> 0
                new_val = 1 if current_val == 0 else 0
                return find_kth(row - 1, pos - half, new_val)
        
        # 从第n行开始，初始值为0（第一行总是0），位置为k
        return find_kth(n, k, 0)
