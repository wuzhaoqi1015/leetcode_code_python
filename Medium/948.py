class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # 对令牌进行排序以便使用贪心策略
        tokens.sort()
        left = 0  # 指向最小令牌的指针
        right = len(tokens) - 1  # 指向最大令牌的指针
        score = 0  # 当前分数
        max_score = 0  # 记录最大分数
        
        # 当还有令牌可用时循环
        while left <= right:
            # 如果当前能量足够购买最小的令牌
            if power >= tokens[left]:
                # 购买最小令牌：消耗能量，增加分数
                power -= tokens[left]
                score += 1
                left += 1
                # 更新最大分数
                max_score = max(max_score, score)
            # 如果分数大于0且还有令牌可用
            elif score > 0:
                # 出售最大令牌：获得能量，减少分数
                power += tokens[right]
                score -= 1
                right -= 1
            # 如果既不能购买也不能出售，结束循环
            else:
                break
        
        return max_score
