class Twitter:
    def __init__(self):
        self.timestamp = 0  # 全局时间戳，用于记录推文顺序
        self.user_tweets = {}  # 用户ID到推文列表的映射，推文格式为(tweetId, timestamp)
        self.user_follows = {}  # 用户ID到关注集合的映射

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 如果用户不存在，初始化其数据结构
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        # 添加推文，使用时间戳确保顺序
        self.user_tweets[userId].append((tweetId, self.timestamp))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # 获取用户自己及其关注者的所有推文
        all_tweets = []
        # 包括用户自己的推文
        if userId in self.user_tweets:
            all_tweets.extend(self.user_tweets[userId])
        # 包括关注者的推文
        if userId in self.user_follows:
            for followeeId in self.user_follows[userId]:
                if followeeId in self.user_tweets:
                    all_tweets.extend(self.user_tweets[followeeId])
        # 按时间戳降序排序，取前10条
        all_tweets.sort(key=lambda x: x[1], reverse=True)
        return [tweet[0] for tweet in all_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        # 用户不能关注自己
        if followerId == followeeId:
            return
        # 如果关注者不存在，初始化其关注集合
        if followerId not in self.user_follows:
            self.user_follows[followerId] = set()
        # 添加关注
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # 如果关注者存在且关注了被关注者，则取消关注
        if followerId in self.user_follows and followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)
