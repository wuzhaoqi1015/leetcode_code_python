class TweetCounts:

    def __init__(self):
        self.tweets = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.tweets:
            self.tweets[tweetName] = []
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.tweets:
            return []
        
        if freq == "minute":
            delta = 60
        elif freq == "hour":
            delta = 3600
        else:  # day
            delta = 86400
        
        n = (endTime - startTime) // delta + 1
        result = [0] * n
        
        times = self.tweets[tweetName]
        for t in times:
            if startTime <= t <= endTime:
                idx = (t - startTime) // delta
                result[idx] += 1
        
        return result
