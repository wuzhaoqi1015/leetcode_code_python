class Solution:
    def compress(self, chars: List[str]) -> int:
        # 使用双指针法，一个指针用于遍历，一个指针用于写入压缩后的结果
        write = 0  # 写入位置指针
        read = 0   # 读取位置指针
        n = len(chars)
        
        while read < n:
            char = chars[read]
            count = 0
            
            # 统计连续相同字符的数量
            while read < n and chars[read] == char:
                read += 1
                count += 1
            
            # 写入字符
            chars[write] = char
            write += 1
            
            # 如果计数大于1，写入计数
            if count > 1:
                # 将计数转换为字符串并逐个写入
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        # 返回压缩后的新长度
        return write
