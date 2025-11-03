class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # 存储键值对
        self.order = collections.OrderedDict()  # 维护访问顺序

    def get(self, key: int) -> int:
        if key in self.cache:
            # 更新访问顺序
            self.order.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 更新已存在的键值
            self.cache[key] = value
            self.order.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                # 移除最久未使用的元素
                oldest_key = next(iter(self.order))
                del self.cache[oldest_key]
                del self.order[oldest_key]
            # 添加新元素
            self.cache[key] = value
            self.order[key] = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
