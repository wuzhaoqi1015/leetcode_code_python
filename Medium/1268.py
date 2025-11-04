class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # 首先对产品列表进行字典序排序
        products.sort()
        result = []
        prefix = ""
        # 遍历搜索词的每个字符
        for char in searchWord:
            prefix += char
            temp = []
            # 遍历排序后的产品列表
            for product in products:
                # 检查产品是否以当前前缀开头
                if product.startswith(prefix):
                    temp.append(product)
                # 如果已经找到3个匹配的产品，提前结束
                if len(temp) == 3:
                    break
            result.append(temp)
        return result
