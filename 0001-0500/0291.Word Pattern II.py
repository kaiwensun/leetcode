class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p2s = {}
        s2p = {}
        def dfs(p_index, s_index):
            if p_index >= len(pattern) or s_index >= len(str):
                return p_index == len(pattern) and s_index == len(str)
            c = pattern[p_index]
            word = p2s.get(c)
            if word:
                return s2p.get(word) == c and word == str[s_index:s_index + len(word)] and dfs(p_index + 1, s_index + len(word))
            for s_end in xrange(s_index + 1, len(str) + 1):
                word = str[s_index:s_end]
                if word in s2p:
                    continue
                p2s[c] = word
                s2p[word] = c
                if dfs(p_index + 1, s_end):
                    return True
                del p2s[c]
                del s2p[word]
            return False
        return dfs(0, 0)

