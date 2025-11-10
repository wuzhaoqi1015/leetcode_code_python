class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # 初始化三种停车位的数量
        self.parking_spaces = {
            1: big,    # 大车位数量
            2: medium, # 中车位数量  
            3: small   # 小车位数量
        }

    def addCar(self, carType: int) -> bool:
        # 检查对应类型车位是否可用
        if self.parking_spaces[carType] > 0:
            # 有空车位，减少一个并返回True
            self.parking_spaces[carType] -= 1
            return True
        else:
            # 没有空车位，返回False
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
