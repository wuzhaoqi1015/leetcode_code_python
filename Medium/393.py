class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # 当前需要处理的后续字节数量
        remaining_bytes = 0
        
        for num in data:
            # 只取最低8位
            byte = num & 0xFF
            
            if remaining_bytes == 0:
                # 判断首字节的类型
                if (byte >> 5) == 0b110:  # 2字节字符
                    remaining_bytes = 1
                elif (byte >> 4) == 0b1110:  # 3字节字符
                    remaining_bytes = 2
                elif (byte >> 3) == 0b11110:  # 4字节字符
                    remaining_bytes = 3
                elif (byte >> 7) != 0:  # 1字节字符的最高位必须为0
                    return False
            else:
                # 后续字节必须以10开头
                if (byte >> 6) != 0b10:
                    return False
                remaining_bytes -= 1
        
        # 所有字节处理完毕后，remaining_bytes应该为0
        return remaining_bytes == 0
