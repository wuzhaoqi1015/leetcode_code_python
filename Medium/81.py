class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            # 当左边界与中间值相等时，无法判断哪边有序，缩小左边界
            if nums[left] == nums[mid]:
                left += 1
                continue
            # 左半部分有序
            if nums[left] < nums[mid]:
                # 目标值在有序的左半部分
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右半部分有序
            else:
                # 目标值在有序的右半部分
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
