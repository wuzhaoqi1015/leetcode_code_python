class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_duration = releaseTimes[0]  # 初始化最大持续时间为第一个按键的持续时间
        result_char = keysPressed[0]    # 初始化结果为第一个按键字符
        
        # 遍历从第二个按键开始的所有按键
        for i in range(1, len(releaseTimes)):
            # 计算当前按键的持续时间
            current_duration = releaseTimes[i] - releaseTimes[i-1]
            
            # 如果当前持续时间大于已知最大持续时间
            if current_duration > max_duration:
                max_duration = current_duration
                result_char = keysPressed[i]
            # 如果持续时间相同但当前字符按字母顺序更大
            elif current_duration == max_duration and keysPressed[i] > result_char:
                result_char = keysPressed[i]
        
        return result_char
