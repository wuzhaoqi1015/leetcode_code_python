class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.price_map = {}
        # 创建商品到价格的映射字典
        for i in range(len(products)):
            self.price_map[products[i]] = prices[i]
        self.customer_count = 0  # 顾客计数器

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0.0
        # 计算商品总价
        for i in range(len(product)):
            product_id = product[i]
            product_amount = amount[i]
            total += self.price_map[product_id] * product_amount
        
        self.customer_count += 1
        # 检查是否达到打折条件
        if self.customer_count % self.n == 0:
            # 应用折扣
            total = total * (100 - self.discount) / 100.0
        
        return total
