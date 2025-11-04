class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # 预处理，过滤掉本身包含重复字符的字符串
        unique_arr = []
        for s in arr:
            if len(s) == len(set(s)):
                unique_arr.append(s)
        
        # 将每个字符串转换为位掩码
        masks = []
        for s in unique_arr:
            mask = 0
            for char in s:
                # 将字符映射到位掩码的相应位置
                mask |= 1 << (ord(char) - ord('a'))
            masks.append(mask)
        
        self.max_len = 0
        
        def backtrack(index, current_mask, current_length):
            # 更新最大长度
            self.max_len = max(self.max_len, current_length)
            
            # 遍历剩余字符串
            for i in range(index, len(masks)):
                # 检查当前字符串是否与已选字符串有重复字符
                if current_mask & masks[i] == 0:
                    # 无重复，继续递归
                    backtrack(i + 1, current_mask | masks[i], current_length + len(unique_arr[i]))
        
        # 从第一个字符串开始回溯
        backtrack(0, 0, 0)
        return self.max_len
