class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # 如果没有投票，直接返回空字符串
        if not votes:
            return ""
        
        # 获取所有参赛团队（从第一个投票字符串中获取所有唯一字符）
        teams = list(votes[0])
        n = len(teams)  # 团队数量
        
        # 初始化计数字典，键为团队，值为长度为n的列表，记录每个排位的得票数
        vote_count = {team: [0] * n for team in teams}
        
        # 统计每个团队在每个排位的得票数
        for vote in votes:
            for idx, team in enumerate(vote):
                vote_count[team][idx] += 1
        
        # 自定义排序函数
        def sort_key(team):
            # 返回一个元组，包含该团队在所有排位的得票数（负数用于降序排列）
            # 最后加上团队名称用于字母顺序排序
            return tuple(-vote_count[team][i] for i in range(n)) + (team,)
        
        # 对团队进行排序
        sorted_teams = sorted(teams, key=sort_key)
        
        # 将排序后的团队列表连接成字符串返回
        return ''.join(sorted_teams)
