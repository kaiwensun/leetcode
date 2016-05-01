"""
Basic idea:
	Dynamic Programming
	Store the least number of coins required to make up i, for each i<amount

180 / 180 test cases passed.
Status: Accepted
Runtime: 912 ms
Sorry. We do not have enough accepted submissions.
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()    #sort for pruning when i-c<0
        table = [amount+1]*(amount+1)    #table[i-1] indicates the least number of coins to makeup amount i
        table[0]=0
        for i in xrange(1,amount+1):
            for c in coins:
                if i-c<0:
                    break
                if table[i-c]+1<table[i]:
                    table[i]=table[i-c]+1
        return table[amount] if table[amount]<=amount else -1

