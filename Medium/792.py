class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # 使用字典记录每个字符在s中出现的位置
        char_positions = defaultdict(list)
        for idx, char in enumerate(s):
            char_positions[char].append(idx)
        
        count = 0
        # 遍历每个单词检查是否为子序列
        for word in words:
            # 当前在s中查找的起始位置
            current_pos = -1
            is_subseq = True
            
            for char in word:
                # 在char_positions中查找第一个大于current_pos的位置
                positions = char_positions[char]
                # 使用二分查找找到第一个大于current_pos的位置
                left, right = 0, len(positions) - 1
                found_pos = -1
                
                while left <= right:
                    mid = (left + right) // 2
                    if positions[mid] > current_pos:
                        found_pos = positions[mid]
                        right = mid - 1
                    else:
                        left = mid + 1
                
                if found_pos == -1:
                    is_subseq = False
                    break
                else:
                    current_pos = found_pos
            
            if is_subseq:
                count += 1
        
        return count
