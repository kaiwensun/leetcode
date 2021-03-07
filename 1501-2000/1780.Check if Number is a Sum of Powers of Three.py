powers = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969]
valid = set()
def dfs(i, sm):
    if sm > 10 ** 7:
        return
    if i == len(powers):
        valid.add(sm)
    else:
        dfs(i + 1, sm)
        dfs(i + 1, sm + powers[i])

dfs(0, 0)

class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n in valid

