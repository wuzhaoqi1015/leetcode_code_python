class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # 创建一个字典来存储order中每个字符的索引作为排序权重
        order_dict = {}
        for idx, char in enumerate(order):
            order_dict[char] = idx
        
        # 将s中的字符分为在order中的和不在order中的
        in_order = []
        not_in_order = []
        for char in s:
            if char in order_dict:
                in_order.append(char)
            else:
                not_in_order.append(char)
        
        # 对在order中的字符按照order中的顺序进行排序
        in_order.sort(key=lambda x: order_dict[x])
        
        # 将排序后的字符与不在order中的字符拼接
        result = ''.join(in_order) + ''.join(not_in_order)
        return result
