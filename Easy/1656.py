class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.ptr = 1  # 当前指针初始化为1
        self.stream = [None] * (n + 1)  # 创建存储空间，索引从1到n

    def insert(self, idKey: int, value: str) -> List[str]:
        # 将值存入对应id位置
        self.stream[idKey] = value
        result = []
        
        # 如果当前指针位置有值，则开始连续收集
        if idKey == self.ptr:
            # 从ptr开始连续收集直到遇到空值
            while self.ptr <= self.n and self.stream[self.ptr] is not None:
                result.append(self.stream[self.ptr])
                self.ptr += 1
                
        return result
