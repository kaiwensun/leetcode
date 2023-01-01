"""
Sundaram 筛法（Sieve of Sundaram）

https://www.cnblogs.com/kentle/p/14205126.html


1. Sundaram 筛法步骤
Sundaram 筛法使用了一种特殊的方法，绕过所有偶数，筛去所有的奇合数

给定一个正整数 n，令 k = [𝑛−12]（方括号 [ ] 表示下取整）
将所有不超过 k 的形如 𝑖+𝑗+2⋅𝑖⋅𝑗,𝑖,𝑗∈𝑍+ 的整数标记
记剩下的不超过 k 且未被标记的整数集合为 A
如果 n ≥ 2，则返回 {2}⋃{2𝑞+1|𝑞∈𝐴,𝑞≠0}
否则返回空集
2. Sundaram 筛法原理
Sundaram 筛法并没有考虑偶数的情况，它将奇合数全部筛去，剩余的大于 1 的奇数便都是素数
Sundaram 筛法的标记数组将数组下标 i 映射到 2i+1，即 0 号位对应整数 1，1 号位对应整数 3
对于奇合数 q，有 q = n1·n2 = (2i + 1)·(2j + 1) = 2i + 2j + 4ij + 1，对应的下标为 (q - 1) / 2 = i + j + 2ij
从上述推导过程也可知，下标 i + j + 2ij 对应的整数 q 必定为合数
故可以通过筛去对应下标 i + j + 2ij 的整数来筛去奇合数
此外，对于正整数 n，不超过 n 的奇数有 k = [𝑛−12] 个
对于不超过 k 的 i + j + 2ij，在遍历过程中，若将 i 作为外层循环，j 作为内层循环，那么可以通过如下循环遍历
for i in range(1, k + 1):
    for j in range(1, k + 1):
        if i + j + 2 * i * j <= k:
            # 筛去 i+j+2ij 对应整数
不难发现，i 与 j 具有对称性，若 j 仍从 1 开始循环，那么会产生较多重复。当 i = m ，j = 1, 2, ..., m-1 时，其实等价于 i = 1, 2, ..., m-1, j = 1，因为二者对应的 i + j + 2ij 的值相等，筛去的都是同一个整数，且后者在 i = m 之前已经被遍历过。故可以让 j 从 i 开始遍历，减少重复遍历的次数。即：
for i in range(1, k + 1):
    for j in range(i, k + 1):
        if i + j + 2 * i * j <= k:
            # 筛去 i+j+2ij 对应整数
对于 i 和 j 的范围，我们还能够再优化一下
当 j = i 的时候，有 i + j + 2ij = 2i · (i + 1)，这是内层遍历过程中筛去的下标最小值，同时该值也随着 i 的循环而递增。一旦该值超过了整数 k，那么之后的 i + j + 2ij 的值均会超过 k。因此，令 2i · (i + 1) ≤ k，可以解出 i 的最大值为 1+2𝑘√−12。借此可以对外层 i 的循环进行优化
同时，可以发现，i + j + 2ij = i + (2i + 1) · j，若将 i 视为定值，则上式是以2i · (i + 1) 为首项，以 (2i + 1) 为公差的等差数列。那么根据这点可以对内层循环进行优化
for i in range(1, int((sqrt(1 + 2 * k) - 1) / 2) + 1):
    for j in range(2 * i *(i + 1), k + 1, 2 * i + 1):
        # 筛去 j 对于整数
"""

import bisect

def sieve_of_sundaram(mx):
    if mx < 2:
        return []
    mx_idx = (mx - 1) // 2
    is_prime_idx = [True] * (mx_idx + 1)
    for i in range(1, len(is_prime_idx)):
        if 2 * i * i + i + i > mx_idx:
            break
        for j in range(i, len(is_prime_idx)):
            if 2 * i * j + i + j > mx_idx:
                break
            else:
                is_prime_idx[2 * i * j + i + j] = False
    return [2] + [2 * i + 1 for i, is_prime in enumerate(is_prime_idx) if is_prime and i > 0]

MAX = 10 ** 6
PRIMES = sieve_of_sundaram(MAX)

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        l = bisect.bisect_left(PRIMES, left)
        diff = float("inf")
        res_ind = -1
        for i in range(l, len(PRIMES) - 1):
            if PRIMES[i + 1] > right:
                break
            new_diff = PRIMES[i + 1] - PRIMES[i]
            if new_diff < diff:
                diff = new_diff
                res_ind = i
                if diff == 2:
                    break
        if res_ind == -1:
            return [-1, -1]
        return [PRIMES[res_ind], PRIMES[res_ind + 1]]

