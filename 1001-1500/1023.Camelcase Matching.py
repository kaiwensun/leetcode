class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        pattern = [''] + list(pattern) + ['']
        pattern = '^' + '[a-z]*'.join(pattern) + '$'
        print(pattern)
        checker = re.compile(pattern)
        return map(bool, map(checker.match, queries))
