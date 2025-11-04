class TimeMap:

    def __init__(self):
        # 使用字典存储键值对，每个键对应一个列表，列表中存储(时间戳, 值)元组
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # 如果键不存在，创建新的列表
        if key not in self.store:
            self.store[key] = []
        # 由于时间戳严格递增，直接添加到列表末尾
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # 如果键不存在，返回空字符串
        if key not in self.store:
            return ""
        
        # 获取该键对应的所有时间戳-值对
        pairs = self.store[key]
        
        # 二分查找最大的小于等于给定时间戳的时间戳
        left, right = 0, len(pairs) - 1
        result = ""
        
        while left <= right:
            mid = (left + right) // 2
            if pairs[mid][0] <= timestamp:
                result = pairs[mid][1]  # 更新结果为当前找到的值
                left = mid + 1  # 继续向右查找更大的时间戳
            else:
                right = mid - 1  # 向左查找
                
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
