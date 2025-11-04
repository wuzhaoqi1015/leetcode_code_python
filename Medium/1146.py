class SnapshotArray:

    def __init__(self, length: int):
        # 使用字典列表存储每个索引的历史记录
        self.data = [dict() for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        # 在当前快照ID下设置索引的值
        self.data[index][self.snap_id] = val

    def snap(self) -> int:
        # 创建快照并返回快照ID
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # 获取指定索引在指定快照ID时的值
        # 如果该快照ID不存在，则查找最近的小于等于该快照ID的值
        history = self.data[index]
        if snap_id in history:
            return history[snap_id]
        
        # 二分查找最近的小于等于snap_id的快照
        keys = sorted(history.keys())
        left, right = 0, len(keys) - 1
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if keys[mid] <= snap_id:
                result = history[keys[mid]]
                left = mid + 1
            else:
                right = mid - 1
                
        return result


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
