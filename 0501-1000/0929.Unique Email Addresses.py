class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+', 1)[0].replace('.', '')
            result.add((local, domain))
        return len(result)
