class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            # 提取年龄部分（第11-12个字符，索引10-11）
            age_str = detail[11:13]
            age = int(age_str)
            if age > 60:
                count += 1
        return count
