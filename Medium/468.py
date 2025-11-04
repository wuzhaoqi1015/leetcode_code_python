class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # 检查IPv4地址
        if '.' in queryIP:
            parts = queryIP.split('.')
            # IPv4必须有4个部分
            if len(parts) != 4:
                return "Neither"
            for part in parts:
                # 每个部分不能为空
                if not part:
                    return "Neither"
                # 检查是否包含非数字字符
                if not part.isdigit():
                    return "Neither"
                # 检查前导零
                if len(part) > 1 and part[0] == '0':
                    return "Neither"
                # 检查数值范围
                num = int(part)
                if num < 0 or num > 255:
                    return "Neither"
            return "IPv4"
        
        # 检查IPv6地址
        elif ':' in queryIP:
            parts = queryIP.split(':')
            # IPv6必须有8个部分
            if len(parts) != 8:
                return "Neither"
            for part in parts:
                # 每个部分长度必须在1-4之间
                if len(part) < 1 or len(part) > 4:
                    return "Neither"
                # 检查每个字符是否都是合法的十六进制字符
                for char in part:
                    if not (char.isdigit() or 'a' <= char <= 'f' or 'A' <= char <= 'F'):
                        return "Neither"
            return "IPv6"
        
        # 既不是IPv4也不是IPv6
        else:
            return "Neither"
