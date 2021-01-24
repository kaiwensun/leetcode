class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        languages = map(set, languages)
        friendships = [(u, v) for u, v in friendships if not languages[u - 1] & languages[v - 1]]
        friendships.sort()
        opt_res = float("inf")
        for language in xrange(1, n + 1):
            language_users = set()
            res = 0
            for u, v in friendships:
                for user in u, v:
                    if not (language in languages[user - 1] or user in language_users):
                        language_users.add(user)
                        res += 1
            opt_res = min(opt_res, res)
        return opt_res

