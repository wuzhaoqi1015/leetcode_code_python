class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        # 初始化变量
        minimum = -1
        maximum = -1
        total_sum = 0
        total_count = 0
        max_freq = 0
        mode = -1
        
        # 遍历count数组计算统计量
        for num, freq in enumerate(count):
            if freq > 0:
                # 更新最小值
                if minimum == -1:
                    minimum = num
                # 更新最大值
                maximum = num
                # 更新总和和总个数
                total_sum += num * freq
                total_count += freq
                # 更新众数
                if freq > max_freq:
                    max_freq = freq
                    mode = num
        
        # 计算均值
        mean = total_sum / total_count
        
        # 计算中位数
        median = 0.0
        # 找到中间位置
        mid1 = (total_count + 1) // 2
        mid2 = (total_count + 2) // 2
        cnt = 0
        first_median = -1
        second_median = -1
        
        for num, freq in enumerate(count):
            if freq == 0:
                continue
            # 检查是否到达第一个中间位置
            if first_median == -1 and cnt + freq >= mid1:
                first_median = num
            # 检查是否到达第二个中间位置
            if second_median == -1 and cnt + freq >= mid2:
                second_median = num
                break
            cnt += freq
        
        # 根据总个数的奇偶性计算中位数
        if total_count % 2 == 1:
            median = first_median
        else:
            median = (first_median + second_median) / 2.0
        
        # 返回结果数组
        return [float(minimum), float(maximum), float(mean), float(median), float(mode)]
