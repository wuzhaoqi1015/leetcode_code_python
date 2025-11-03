class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 如果只有一行或者行数大于等于字符串长度，直接返回原字符串
        if numRows == 1 or numRows >= len(s):
            return s
            
        # 创建存储每行字符的列表
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # 遍历字符串中的每个字符
        for char in s:
            # 将当前字符添加到对应行
            rows[current_row] += char
            
            # 当到达第一行或最后一行时，改变方向
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            # 根据方向更新当前行
            current_row += 1 if going_down else -1
        
        # 将所有行的字符连接起来
        return ''.join(rows)
