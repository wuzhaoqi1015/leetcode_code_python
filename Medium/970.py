class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        # 使用集合来存储结果，避免重复值
        res = set()
        # 处理x=1和y=1的特殊情况，避免无限循环
        max_i = 0 if x == 1 else bound
        max_j = 0 if y == 1 else bound
        
        # 遍历所有可能的指数组合
        i = 0
        while True:
            # 计算x的i次方
            if x == 1:
                val_x = 1
            else:
                val_x = x ** i
                if val_x > bound:
                    break
            
            j = 0
            while True:
                # 计算y的j次方
                if y == 1:
                    val_y = 1
                else:
                    val_y = y ** j
                    if val_y > bound:
                        break
                
                # 计算强整数
                total = val_x + val_y
                if total <= bound:
                    res.add(total)
                else:
                    break
                
                # 如果y=1，只需要计算一次j
                if y == 1:
                    break
                j += 1
            
            # 如果x=1，只需要计算一次i
            if x == 1:
                break
            i += 1
        
        # 将集合转换为列表返回
        return list(res)
