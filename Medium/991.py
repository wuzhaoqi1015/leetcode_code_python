class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # 从target反向操作到startValue
        # 反向操作：如果target是偶数则除以2，否则加1
        operations = 0
        while target > startValue:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
            operations += 1
        # 当target <= startValue时，只能通过递减操作
        return operations + (startValue - target)
