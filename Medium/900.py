class RLEIterator:

    def __init__(self, encoding: List[int]):
        # 存储编码数组
        self.encoding = encoding
        # 当前指向的编码对索引
        self.index = 0
        # 当前编码对中剩余的计数
        self.count = 0
        # 如果初始编码数组不为空，初始化第一个编码对的计数
        if self.encoding:
            self.count = self.encoding[self.index]

    def next(self, n: int) -> int:
        # 遍历编码数组，直到满足n个元素或遍历完成
        while n > 0 and self.index < len(self.encoding):
            # 如果当前编码对的剩余计数大于等于n
            if self.count >= n:
                # 消耗n个计数
                self.count -= n
                # 返回当前编码对的值
                return self.encoding[self.index + 1]
            else:
                # 消耗当前编码对的所有剩余计数
                n -= self.count
                self.count = 0
                # 移动到下一个编码对
                self.index += 2
                # 如果还有下一个编码对，更新计数
                if self.index < len(self.encoding):
                    self.count = self.encoding[self.index]
        # 如果没有足够的元素，返回-1
        return -1
