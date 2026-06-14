from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.posts = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
        self.timestamp += 1
        self.posts[userId].append((-self.timestamp, tweetId))

        if userId not in self.following:
            self.following[userId] = set()

    def getNewsFeed(self, userId: int) -> List[int]:
        followee_set = self.following.get(userId, set())
        all_posts = list(self.posts.get(userId, []))

        for followee in followee_set:
            all_posts.extend(self.posts.get(followee, []))
        
        heapq.heapify(all_posts)

        feed = []
        for _ in range(10):
            if all_posts:
                feed.append(heapq.heappop(all_posts)[1])

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
        