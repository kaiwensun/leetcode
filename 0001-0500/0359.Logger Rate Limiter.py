import collections

class Logger:
    
    DELTA = 10

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        self.messages = set()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        while self.queue and self.queue[0][0] <= timestamp - Logger.DELTA:
            _, old_msg = self.queue.popleft()
            self.messages.discard(old_msg)
        if message not in self.messages:
            self.messages.add(message)
            self.queue.append((timestamp, message))
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)