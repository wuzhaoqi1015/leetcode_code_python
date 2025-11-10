class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 创建arr2中元素的索引映射
        order_map = {}
        for idx, num in enumerate(arr2):
            order_map[num] = idx
        
        # 自定义排序函数
        def custom_sort(x):
            if x in order_map:
                # 返回在arr2中的索引作为排序依据
                return (0, order_map[x])
            else:
                # 不在arr2中的元素放在后面，按值升序排序
                return (1, x)
        
        # 对arr1进行排序
        arr1.sort(key=custom_sort)
        return arr1
