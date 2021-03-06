class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def find_palindromes(i, j):
            while 0 <= i <= j < len(s) and s[i] == s[j]:
                palindrome[i].append(j + 1)
                i -= 1
                j += 1
        
        def split(i, acc):
            if i == len(s):
                res.append(list(acc))
            else:
                for j in palindrome[i]:
                    acc.append(s[i:j])
                    split(j, acc)
                    acc.pop()

        palindrome = [[] for _ in xrange(len(s))]
        for i in xrange(len(s)):
            find_palindromes(i, i)
            find_palindromes(i, i + 1)

        res = []
        split(0, [])
        return res

