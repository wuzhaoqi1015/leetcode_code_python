from collections import deque, Counter

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(friends)
        visited = [False] * n
        queue = deque()
        queue.append((id, 0))
        visited[id] = True
        target_level_friends = []
        
        # BFS to find friends at exactly the given level
        while queue:
            current_id, current_level = queue.popleft()
            if current_level == level:
                target_level_friends.append(current_id)
                continue
            if current_level > level:
                break
                
            for friend_id in friends[current_id]:
                if not visited[friend_id]:
                    visited[friend_id] = True
                    queue.append((friend_id, current_level + 1))
        
        # Collect all videos watched by target level friends
        video_counter = Counter()
        for friend_id in target_level_friends:
            for video in watchedVideos[friend_id]:
                video_counter[video] += 1
        
        # Sort videos by frequency (ascending), then by name (ascending)
        sorted_videos = sorted(video_counter.keys(), key=lambda x: (video_counter[x], x))
        
        return sorted_videos
