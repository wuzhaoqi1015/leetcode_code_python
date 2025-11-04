class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        from collections import defaultdict
        
        # 使用字典记录每行被预约的座位
        reserved_dict = defaultdict(set)
        for row, seat in reservedSeats:
            reserved_dict[row].add(seat)
        
        result = 0
        
        # 处理有预约座位的行
        for row in reserved_dict:
            reserved = reserved_dict[row]
            # 检查三个可能的四人座位区域
            # 区域1: 座位2-5
            area1 = not any(seat in reserved for seat in [2, 3, 4, 5])
            # 区域2: 座位4-7  
            area2 = not any(seat in reserved for seat in [4, 5, 6, 7])
            # 区域3: 座位6-9
            area3 = not any(seat in reserved for seat in [6, 7, 8, 9])
            
            # 如果区域1和区域3都可用，可以安排两个家庭
            if area1 and area3:
                result += 2
            # 如果区域1、区域2、区域3中任意一个可用，安排一个家庭
            elif area1 or area2 or area3:
                result += 1
        
        # 处理没有预约座位的行，每行可以安排两个家庭
        result += (n - len(reserved_dict)) * 2
        
        return result
