from collections import deque

class AuthenticationManager(object):

    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        self.timeToLive = timeToLive
        self.queue = deque()
        self.latest = {}


    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        self.queue.append((tokenId, currentTime))
        self.latest[tokenId] = currentTime


    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        if self.latest.get(tokenId, float("-inf")) + self.timeToLive > currentTime:
            self.generate(tokenId, currentTime)


    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """
        while self.queue and self.queue[0][1] <= currentTime - self.timeToLive:
            tokenId, thenTime = self.queue.popleft()
            if self.latest[tokenId] == thenTime:
                del self.latest[tokenId]
        return len(self.latest)



# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)

