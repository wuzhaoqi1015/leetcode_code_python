class Solution:
    def entityParser(self, text: str) -> str:
        # 定义HTML实体到对应字符的映射字典
        entity_map = {
            '&quot;': '"',
            '&apos;': "'",
            '&amp;': '&',
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/'
        }
        
        result = []  # 用于存储解析结果的字符列表
        i = 0  # 文本遍历索引
        n = len(text)
        
        while i < n:
            # 如果当前字符是'&'，可能是一个实体开始
            if text[i] == '&':
                # 查找实体结束的分号';'
                j = i
                while j < n and text[j] != ';':
                    j += 1
                
                # 如果找到了分号，检查这个实体是否在映射中
                if j < n and text[j] == ';':
                    entity = text[i:j+1]  # 提取完整的实体
                    # 如果实体在映射中，替换为对应字符
                    if entity in entity_map:
                        result.append(entity_map[entity])
                        i = j + 1  # 跳过整个实体
                        continue
            
            # 如果不是实体或者实体不在映射中，直接添加当前字符
            result.append(text[i])
            i += 1
        
        # 将字符列表连接成字符串返回
        return ''.join(result)
