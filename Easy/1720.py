class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # 初始化结果数组，第一个元素已知
        arr = [first]
        # 遍历编码数组，逐个解码
        for i in range(len(encoded)):
            # 根据异或性质：a XOR b = c 等价于 a XOR c = b
            # 已知arr[i]和encoded[i]，可以求出arr[i+1]
            next_val = arr[i] ^ encoded[i]
            arr.append(next_val)
        return arr
