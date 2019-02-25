from collections import Counter
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        result = Counter()
        for cpdomain in cpdomains:
            cnt, dom = cpdomain.split(' ')
            cnt = int(cnt)
            result[dom] += cnt
            subdomain = dom.split('.', 1)
            while len(subdomain) == 2:
                subdomain = subdomain[1]
                result[subdomain] += cnt
                subdomain = subdomain.split('.', 1)
        return ['{} {}'.format(cnt, dom) for dom, cnt in result.iteritems()]
