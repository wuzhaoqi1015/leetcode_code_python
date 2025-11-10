class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        n = len(player1)
        
        def calculate_score(player):
            score = 0
            # 记录前两轮是否有10分
            prev_strike = [False] * 2  # 索引0表示前一轮，索引1表示前两轮
            
            for i in range(n):
                current_score = player[i]
                # 检查前两轮是否有strike
                if prev_strike[0] or prev_strike[1]:
                    score += 2 * current_score
                else:
                    score += current_score
                
                # 更新strike记录
                # 将当前轮的状态加入记录
                if current_score == 10:
                    # 移动记录：当前轮成为新的前一轮，前一轮成为前两轮
                    prev_strike[1] = prev_strike[0]
                    prev_strike[0] = True
                else:
                    # 移动记录，但当前轮不是strike
                    prev_strike[1] = prev_strike[0]
                    prev_strike[0] = False
        
            return score
        
        score1 = calculate_score(player1)
        score2 = calculate_score(player2)
        
        if score1 > score2:
            return 1
        elif score2 > score1:
            return 2
        else:
            return 0
