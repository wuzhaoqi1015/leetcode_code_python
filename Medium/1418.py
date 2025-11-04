from typing import List
from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # 使用集合来收集所有不同的食物名称
        food_items = set()
        # 使用字典来记录每桌点的每种食物的数量
        # 外层字典的key是桌号，内层字典的key是食物名称，value是数量
        table_orders = defaultdict(lambda: defaultdict(int))
        
        # 遍历所有订单
        for order in orders:
            # 订单格式: [customerName, tableNumber, foodItem]
            table_num = order[1]
            food_name = order[2]
            
            # 将食物名称添加到集合中
            food_items.add(food_name)
            # 增加该桌该食物的计数
            table_orders[table_num][food_name] += 1
        
        # 将食物名称按字母顺序排序
        sorted_foods = sorted(food_items)
        
        # 构建结果列表
        result = []
        
        # 添加表头
        header = ["Table"] + sorted_foods
        result.append(header)
        
        # 将桌号转换为整数进行排序，然后按升序排列
        sorted_tables = sorted(table_orders.keys(), key=int)
        
        # 为每桌添加一行数据
        for table in sorted_tables:
            row = [table]  # 第一列是桌号
            # 为每种食物添加对应的数量
            for food in sorted_foods:
                count = table_orders[table].get(food, 0)
                row.append(str(count))
            result.append(row)
        
        return result
