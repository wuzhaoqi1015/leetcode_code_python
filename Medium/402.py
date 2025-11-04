class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 使用单调栈来维护最小数字序列
        stack = []
        # 遍历字符串中的每个数字
        for digit in num:
            # 当栈不为空且还有移除次数且栈顶数字大于当前数字时，弹出栈顶
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            # 将当前数字压入栈中
            stack.append(digit)
        # 如果还有剩余的移除次数，从栈顶移除剩余的数字
        if k > 0:
            stack = stack[:-k]
        # 将栈中数字连接成字符串，并去除前导零
        result = ''.join(stack).lstrip('0')
        # 如果结果为空字符串，返回"0"
        return result if result else "0"
