class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n = len(num)
        # 尝试不同的前两个数字组合
        for i in range(1, min(11, n)):  # 第一个数字最多10位（2^31是10位数）
            if i > 1 and num[0] == '0':  # 不能有前导零，除非是0本身
                break
            first = int(num[:i])
            if first > 2**31 - 1:  # 检查是否超出32位整数范围
                continue
                
            for j in range(i + 1, min(i + 11, n)):  # 第二个数字最多10位
                if j - i > 1 and num[i] == '0':  # 不能有前导零，除非是0本身
                    break
                second = int(num[i:j])
                if second > 2**31 - 1:  # 检查是否超出32位整数范围
                    continue
                    
                # 开始构建斐波那契序列
                fib = [first, second]
                k = j
                while k < n:
                    # 计算下一个斐波那契数
                    next_val = fib[-1] + fib[-2]
                    if next_val > 2**31 - 1:  # 检查是否超出范围
                        break
                    next_str = str(next_val)
                    # 检查剩余字符串是否以next_str开头
                    if num.startswith(next_str, k):
                        fib.append(next_val)
                        k += len(next_str)
                    else:
                        break
                else:  # 循环正常结束，说明成功拆分
                    if len(fib) >= 3:  # 确保序列长度至少为3
                        return fib
        return []  # 无法拆分
