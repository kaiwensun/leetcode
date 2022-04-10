const dp = [1, 9];
function countNumbersWithUniqueDigits(n: number): number {
    while (dp.length <= n) {
        dp.push(dp[dp.length - 1] * (11 - dp.length));
    }
    return dp.slice(0, n + 1).reduce((a, b) => a + b, 0);
};

