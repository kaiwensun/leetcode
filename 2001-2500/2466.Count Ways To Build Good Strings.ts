function countGoodStrings(low: number, high: number, zero: number, one: number): number {
    const MOD = 10 ** 9 + 7;
    let res = 0;
    const dp = [1];
    for (let i = 1; i <= high; i++) {
        const pre0 = i - zero < 0 ? 0 : dp[i - zero];
        const pre1 = i - one < 0 ? 0 : dp[i - one];
        dp.push((pre0 + pre1) % MOD);
        if (i >= low) {
            res += dp[dp.length - 1];
            res %= MOD;
        }
    }
    return res;
};

