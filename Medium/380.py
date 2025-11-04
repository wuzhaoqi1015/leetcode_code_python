import random

class RandomizedSet:

    def __init__(self):
        # 使用字典存储值和其在列表中的索引
        self.val_to_index = {}
        # 使用列表存储所有值，用于随机访问
        self.values = []

    def insert(self, val: int) -> bool:
        # 如果值已存在，返回False
        if val in self.val_to_index:
            return False
        # 将值添加到列表末尾，并在字典中记录索引
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        # 如果值不存在，返回False
        if val not in self.val_to_index:
            return False
        
        # 获取要删除值的索引
        index_to_remove = self.val_to_index[val]
        # 获取列表最后一个元素
        last_val = self.values[-1]
        
        # 将最后一个元素移动到要删除的位置
        self.values[index_to_remove] = last_val
        # 更新最后一个元素在字典中的索引
        self.val_to_index[last_val] = index_to_remove
        
        # 删除列表最后一个元素
        self.values.pop()
        # 从字典中删除该值
        del self.val_to_index[val]
        
        return True

    def getRandom(self) -> int:
        # 从列表中随机返回一个元素
        return random.choice(self.values)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
