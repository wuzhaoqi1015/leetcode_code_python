class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)
        # 从大到小依次将每个元素放到正确位置
        for target in range(n, 0, -1):
            # 如果当前元素已经在正确位置，跳过
            if arr[target-1] == target:
                continue
            # 找到目标元素当前的位置
            idx = arr.index(target)
            # 如果目标元素不在首位，先翻转到首位
            if idx != 0:
                result.append(idx+1)
                # 反转前idx+1个元素
                arr[:idx+1] = arr[:idx+1][::-1]
            # 再将目标元素翻转到正确位置
            result.append(target)
            arr[:target] = arr[:target][::-1]
        return result
