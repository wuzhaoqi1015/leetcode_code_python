class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_matches = 0
        current_teams = n
        
        while current_teams > 1:
            if current_teams % 2 == 0:
                # 偶数队伍：进行n/2场比赛，晋级n/2支队伍
                matches = current_teams // 2
                total_matches += matches
                current_teams = matches
            else:
                # 奇数队伍：进行(n-1)/2场比赛，晋级(n-1)/2 + 1支队伍
                matches = (current_teams - 1) // 2
                total_matches += matches
                current_teams = matches + 1
        
        return total_matches
