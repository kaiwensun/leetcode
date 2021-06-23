from datetime import datetime

class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        s = datetime.strptime(startTime, "%H:%M")
        e = datetime.strptime(finishTime, "%H:%M")
        ROUND = 15 * 60
        if 0 <= (e - s).seconds < ROUND:
            return 0
        return int(e.timestamp() // ROUND - (s.timestamp() + ROUND - 60) // ROUND) % (24 * 4)

