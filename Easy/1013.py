class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        # 如果总和不能被3整除，直接返回False
        if total % 3 != 0:
            return False
        
        target = total // 3
        n = len(arr)
        current_sum = 0
        count = 0
        
        # 遍历数组寻找满足条件的三个部分
        for i in range(n):
            current_sum += arr[i]
            # 当累计和等于目标值时，找到一个分割点
            if current_sum == target:
                count += 1
                current_sum = 0
                # 找到两个分割点即可（将数组分为三部分）
                if count == 2 and i < n - 1:
                    return True
        
        return False
