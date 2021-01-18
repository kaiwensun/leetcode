class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_accounts = defaultdict(list)
        for account_id, emails in enumerate(accounts):
            for i in range(1, len(emails)):
                email_to_accounts[emails[i]].append(account_id)
        data = list(range(len(accounts)))
        def find(x):
            if data[x] != x:
                data[x] = find(data[x])
            return data[x]
        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                data[rx] = ry
        for email, ids in email_to_accounts.items():
            for i in range(1, len(ids)):
                union(ids[i], ids[i - 1])
        account_to_emails = defaultdict(set)
        for i in range(len(data)):
            account_to_emails[find(data[i])] |= set(accounts[i][1:])
        return [[accounts[i][0], *sorted(emails)] for i, emails in account_to_emails.items()]

