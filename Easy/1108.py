class Solution:
    def defangIPaddr(self, address: str) -> str:
        # 使用字符串的replace方法将所有"."替换为"[.]"
        return address.replace('.', '[.]')
