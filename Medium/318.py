class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # 将每个单词转换为位掩码表示
        masks = []
        for word in words:
            mask = 0
            for char in word:
                # 将字符映射到位掩码的相应位置
                mask |= 1 << (ord(char) - ord('a'))
            masks.append(mask)
        
        max_product = 0
        n = len(words)
        # 遍历所有单词对
        for i in range(n):
            for j in range(i + 1, n):
                # 检查两个单词是否有公共字母
                if masks[i] & masks[j] == 0:
                    # 计算乘积并更新最大值
                    product = len(words[i]) * len(words[j])
                    if product > max_product:
                        max_product = product
        
        return max_product
