class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        dp = [float('inf')] * (len(books) + 1)
        dp[0] = 0
        for i, book in enumerate(books):
            dp[i + 1] = dp[i] + book[1]
            layer_w = book[0]
            layer_h = book[1]
            for j in xrange(i - 1, -1, -1):
                layer_w += books[j][0]
                if layer_w > shelf_width:
                    break
                layer_h = max(layer_h, books[j][1])
                dp[i + 1] = min(dp[i + 1], dp[j] + layer_h)
        return dp[-1]
