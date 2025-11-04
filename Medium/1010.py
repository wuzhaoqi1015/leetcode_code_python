class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # 初始化一个长度为60的数组，用于记录余数出现的次数
        remainder_count = [0] * 60
        count = 0
        
        # 遍历歌曲持续时间列表
        for t in time:
            # 计算当前歌曲持续时间的余数
            remainder = t % 60
            # 如果余数为0，需要与其它余数为0的歌曲配对
            if remainder == 0:
                count += remainder_count[0]
            else:
                # 否则需要与余数为60-remainder的歌曲配对
                count += remainder_count[60 - remainder]
            # 更新当前余数的计数
            remainder_count[remainder] += 1
            
        return count
