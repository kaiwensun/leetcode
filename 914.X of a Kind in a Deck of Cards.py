class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) <= 1:
            return False
        c = collections.Counter(deck)
        gcd = c[deck[0]]
        for k, v in c.items():
            gcd = math.gcd(gcd, v)
            if gcd == 1:
                return False
        return True
