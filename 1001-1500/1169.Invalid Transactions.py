class Solution(object):
    def invalidTransactions(self, transactions):
        res = []
        transactions = [tr.split(',') for tr in transactions]
        for tr in transactions:
            name, time, amount, city = tr
            amount = int(amount); time = int(time)
            if amount > 1000:
                res.append(tr)
                continue
            for newtr in transactions:
                newname, newtime, newamount, newcity = newtr
                if name != newname:
                    continue
                newtime = int(newtime); newamount = int(newamount)
                if abs(time - newtime) <= 60 and city != newcity:
                    res.append(tr)
                    break
        return [','.join(tr) for tr in res]
