class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counter = collections.Counter()
        for cpdomain in cpdomains:
            cnt, domain = cpdomain.split()
            cnt = int(cnt)
            subdomain = [None, domain]
            while len(subdomain) == 2:
                counter[subdomain[1]] += cnt
                subdomain = subdomain[1].split('.', 1)
        return ['%s %s' % (v, k) for k, v in counter.iteritems()]
