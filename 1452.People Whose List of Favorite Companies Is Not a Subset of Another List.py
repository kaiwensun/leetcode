import collections
class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        company2id = {}
        person2companiesMask = []
        for favList in favoriteCompanies:
            mask = 0
            for i, company in enumerate(favList):
                mask |= 1 << company2id.setdefault(company, len(company2id))
            person2companiesMask.append(mask)
        sortedPersonIds = [p for p, lst in sorted(enumerate(favoriteCompanies), cmp=lambda a, b: len(a[1]) - len(b[1]))]
        res = []
        for i in xrange(len(sortedPersonIds)):
            fail = False
            myPersonId = sortedPersonIds[i]
            myMask = person2companiesMask[myPersonId]
            for j in xrange(i + 1, len(sortedPersonIds)):
                otherPersonId = sortedPersonIds[j]
                otherMask = person2companiesMask[otherPersonId]
                if myMask & otherMask == myMask:
                    fail = True
                    break
            if not fail:
                res.append(myPersonId)
        return sorted(res)
