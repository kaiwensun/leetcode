from sys import stdin
from functools import cache

@cache
def dp(avoid, remains):
    if not any(remains):
        return 1
    if remains[0] + remains[1] + 1 < remains[2]:
        return 0
    res = 0
    for i, remain in enumerate(remains):
        if avoid == i or remains[i] == 0:
            continue
        new_remains = list(remains)
        new_remains[i] -= 1
        res += dp(i, tuple(new_remains))
    return res

for line in stdin:
  nums = tuple(sorted(map(int, line.split())))
  print(dp(-1, nums))

