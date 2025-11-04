class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        n = len(heaters)
        res = 0
        for house in houses:
            left, right = 0, n - 1
            while left < right:
                mid = (left + right) // 2
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid
            if heaters[left] == house:
                continue
            elif heaters[left] < house:
                dist = house - heaters[left]
            else:
                if left > 0:
                    dist = min(heaters[left] - house, house - heaters[left - 1])
                else:
                    dist = heaters[left] - house
            res = max(res, dist)
        return res
