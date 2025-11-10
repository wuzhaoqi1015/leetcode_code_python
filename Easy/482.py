class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # 移除所有破折号并将字母转为大写
        cleaned = s.replace('-', '').upper()
        n = len(cleaned)
        
        # 计算第一组的长度
        first_group_len = n % k
        if first_group_len == 0:
            first_group_len = k
        
        # 构建结果字符串
        result = cleaned[:first_group_len]
        
        # 处理剩余部分，每k个字符为一组
        for i in range(first_group_len, n, k):
            result += '-' + cleaned[i:i+k]
        
        return result
