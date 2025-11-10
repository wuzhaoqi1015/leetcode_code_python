class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # 将字母转换为对应的数字位置，'a'对应1，'b'对应2，依此类推
        col = ord(coordinates[0]) - ord('a') + 1
        # 获取数字部分并转换为整数
        row = int(coordinates[1])
        # 如果列和行的奇偶性相同，则为黑色（返回False），否则为白色（返回True）
        return (col + row) % 2 != 0
