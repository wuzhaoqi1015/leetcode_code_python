import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not re.search(f"{p}", s):
            return False
        else:
            return True if re.search(f"{p}", s).group() == s else False
