class Solution:
    def rotatedDigits(self, n: int) -> int:
        # 定义有效旋转数字映射
        rotate_map = {
            '0': '0',
            '1': '1', 
            '8': '8',
            '2': '5',
            '5': '2',
            '6': '9',
            '9': '6'
        }
        
        count = 0
        # 遍历从1到n的所有数字
        for num in range(1, n + 1):
            num_str = str(num)
            rotated_str = []
            valid = True
            
            # 检查每个数字是否能旋转
            for digit in num_str:
                if digit not in rotate_map:
                    valid = False
                    break
                rotated_str.append(rotate_map[digit])
            
            # 如果是有效旋转且旋转后数字不同，则计数
            if valid and ''.join(rotated_str) != num_str:
                count += 1
                
        return count
