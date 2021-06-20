from datetime import datetime

class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        s = datetime.strptime(startTime, "%H:%M")
        e = datetime.strptime(finishTime, "%H:%M")
        ROUND = 15 * 60
        return int(e.timestamp() // ROUND - (s.timestamp() + ROUND - 1) // ROUND) % (24 * 4)


