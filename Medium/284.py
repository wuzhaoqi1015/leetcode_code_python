class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self._next = None  # 缓存下一个元素
        self._has_next = iterator.hasNext()  # 缓存是否有下一个元素
        if self._has_next:
            self._next = iterator.next()  # 预取第一个元素

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next  # 直接返回缓存的下一个元素

    def next(self):
        """
        :rtype: int
        """
        ret = self._next  # 保存当前要返回的元素
        self._has_next = self.iterator.hasNext()  # 更新是否有下一个元素
        if self._has_next:
            self._next = self.iterator.next()  # 预取下一个元素
        else:
            self._next = None  # 没有下一个元素时清空缓存
        return ret  # 返回当前元素

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._has_next  # 返回是否有下一个元素
