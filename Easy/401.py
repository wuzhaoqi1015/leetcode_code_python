class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # 枚举所有可能的小时和分钟组合
        result = []
        for h in range(12):  # 小时范围0-11
            for m in range(60):  # 分钟范围0-59
                # 计算小时和分钟的二进制中1的个数之和
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    # 格式化分钟，确保两位数显示
                    result.append(f"{h}:{m:02d}")
        return result
