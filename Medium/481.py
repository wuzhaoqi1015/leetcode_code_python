class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1
        # 初始化神奇字符串的前三个字符
        s = [1, 2, 2]
        # 初始化指针，指向下一个要生成的组对应的数字个数在s中的位置
        idx = 2
        # 初始化下一个要添加的数字，1和2交替
        num = 1
        # 初始化1的计数，前三个字符中有一个1
        count = 1
        # 当s长度小于n时继续生成
        while len(s) < n:
            # 当前组应该添加的数字个数
            repeat = s[idx]
            # 添加repeat个num到s中
            for _ in range(repeat):
                s.append(num)
                # 如果添加的是1且总长度不超过n，计数增加
                if num == 1 and len(s) <= n:
                    count += 1
            # 切换数字，1变2，2变1
            num = 3 - num
            # 移动指针到下一个位置
            idx += 1
        return count
