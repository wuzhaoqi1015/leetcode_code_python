class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 使用双指针法，从两端向中间交换元素
        left = 0
        right = len(s) - 1
        while left < right:
            # 交换左右指针指向的元素
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
