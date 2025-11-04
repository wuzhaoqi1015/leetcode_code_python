class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # 使用最大堆来维护当前剩余数量最多的字符
        import heapq
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))
        
        result = []
        
        while heap:
            count1, char1 = heapq.heappop(heap)
            
            # 检查是否连续两个相同字符
            if len(result) >= 2 and result[-1] == char1 and result[-2] == char1:
                if not heap:  # 没有其他字符可用
                    break
                # 取次多的字符
                count2, char2 = heapq.heappop(heap)
                result.append(char2)
                count2 += 1  # 因为使用负数，所以+1相当于减少1
                if count2 < 0:  # 如果还有剩余
                    heapq.heappush(heap, (count2, char2))
                # 把第一个字符放回堆中
                heapq.heappush(heap, (count1, char1))
            else:
                result.append(char1)
                count1 += 1  # 因为使用负数，所以+1相当于减少1
                if count1 < 0:  # 如果还有剩余
                    heapq.heappush(heap, (count1, char1))
        
        return ''.join(result)
