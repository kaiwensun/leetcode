from functools import lru_cache
from collections import defaultdict

MOD = 10 ** 9 + 7
NUM_PEOPLE = 40
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        def genHat2People(person2hats):
            hat2people = [set() for _ in range(NUM_PEOPLE + 1)]
            for person, hats in enumerate(person2hats):
                for hat in hats:
                    hat2people[hat].add(person)
            return hat2people
        @functools.lru_cache(None)
        def search(people_with_hat, hat):
            if hat == NUM_PEOPLE + 1:
                return int(people_with_hat == (1 << len(hats)) - 1)
            res = search(people_with_hat, hat + 1)
            for person in hat2people[hat]:
                if (1 << person) & people_with_hat == 0:
                    res += search((1 << person) | people_with_hat, hat + 1)
                    res %= MOD
            return res
        
        hat2people = genHat2People(hats)
        return search(0, 0)
