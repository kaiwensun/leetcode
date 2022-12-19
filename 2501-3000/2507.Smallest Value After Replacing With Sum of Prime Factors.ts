function getPrimes(upper: number) {
    const nums = new Array(upper + 1).fill(true);
    nums[0] = nums[1] = false;
    const sqrt = Math.sqrt(upper);
    for (let start = 2; start <= sqrt; start++) {
        if (!nums[start]) continue;
        for (let i = start + start; i <= upper; i += start) {
            nums[i] = false;
        }
    }
    return nums.map((prime, i) => prime ? i : 0).filter(i => i);
}

const PRIMES = getPrimes(10 ** 5 * 2);
const PRIME_SET = new Set(PRIMES);

function smallestValue(n: number): number {
    const seen = new Set();
    let res = n;
    while (!PRIME_SET.has(n) && !seen.has(n)) {
        seen.add(n);
        let nxt = 0;
        for (const p of PRIMES) {
            while (n % p === 0) {
                nxt += p;
                n /= p;
            }
            if (n === 1) break;
        }
        n = nxt;
        res = Math.min(res, n);
    }
    return res;
};

