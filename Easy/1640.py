class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # 创建哈希表，以每个piece的第一个元素为键，整个piece为值
        piece_map = {piece[0]: piece for piece in pieces}
        
        i = 0
        while i < len(arr):
            # 如果当前元素不在哈希表中，说明无法匹配任何piece
            if arr[i] not in piece_map:
                return False
            
            # 获取对应的piece
            current_piece = piece_map[arr[i]]
            
            # 逐个比较piece中的元素
            for num in current_piece:
                if i >= len(arr) or arr[i] != num:
                    return False
                i += 1
        
        return True
