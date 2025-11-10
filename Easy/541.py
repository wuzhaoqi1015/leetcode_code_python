class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # 将字符串转换为列表以便进行字符交换
        s_list = list(s)
        n = len(s_list)
        
        # 遍历字符串，步长为2k
        for i in range(0, n, 2 * k):
            left = i
            # 计算需要反转的右边界，取最小值防止越界
            right = min(i + k - 1, n - 1)
            
            # 反转前k个字符
            while left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        
        # 将列表转换回字符串返回
        return ''.join(s_list)
