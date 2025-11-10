class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 使用集合来存储已经遍历过的数字
        seen = set()
        # 遍历数组中的每个元素
        for num in nums:
            # 如果当前数字已经在集合中存在，说明有重复
            if num in seen:
                return True
            # 否则将当前数字添加到集合中
            seen.add(num)
        # 遍历完所有元素都没有重复，返回False
        return False
