class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # 初始化当前海拔和最大海拔
        current_altitude = 0
        max_altitude = 0
        
        # 遍历净海拔高度差数组
        for g in gain:
            # 更新当前海拔
            current_altitude += g
            # 更新最大海拔
            if current_altitude > max_altitude:
                max_altitude = current_altitude
        
        return max_altitude
