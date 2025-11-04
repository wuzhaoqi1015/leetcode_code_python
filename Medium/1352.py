class ProductOfNumbers:

    def __init__(self):
        # 初始化前缀积列表，第一个元素为1便于计算
        self.prefix_products = [1]
        # 记录最近0的位置，初始为-1表示没有0
        self.last_zero = -1
        # 记录当前流中的元素数量
        self.count = 0

    def add(self, num: int) -> None:
        self.count += 1
        # 如果当前数字为0，重置前缀积并记录0的位置
        if num == 0:
            self.prefix_products = [1]
            self.last_zero = self.count
        else:
            # 否则将当前数字乘到最后一个前缀积上
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        # 如果请求的范围包含0，直接返回0
        if self.count - k < self.last_zero:
            return 0
        # 否则通过前缀积计算最后k个数的乘积
        return self.prefix_products[-1] // self.prefix_products[-k-1]
