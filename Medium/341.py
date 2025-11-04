class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # 使用栈来存储迭代器状态，栈顶是当前正在处理的列表
        self.stack = []
        # 将初始列表的迭代器入栈
        self.stack.append(iter(nestedList))
        # 预取下一个整数
        self.next_int = None
    
    def next(self) -> int:
        # 直接返回已经预取到的整数
        result = self.next_int
        # 将next_int置为None，表示需要重新预取
        self.next_int = None
        return result
    
    def hasNext(self) -> bool:
        # 如果已经预取到了整数，直接返回True
        if self.next_int is not None:
            return True
            
        # 当栈不为空时继续寻找下一个整数
        while self.stack:
            try:
                # 获取栈顶迭代器的下一个元素
                element = next(self.stack[-1])
                if element.isInteger():
                    # 如果是整数，保存到next_int并返回True
                    self.next_int = element.getInteger()
                    return True
                else:
                    # 如果是列表，将其迭代器压入栈中
                    self.stack.append(iter(element.getList()))
            except StopIteration:
                # 当前迭代器已耗尽，弹出栈顶
                self.stack.pop()
                
        # 栈为空且没有找到整数，返回False
        return False
