function numberOfWays(s: string): number {
    const buildSize = 3;
    const N = s.length;
    const nums = [].map.call(s, c => parseInt(c)) as number[];
    const dp = new Array(N + 1);
    dp[0] = [0, 0];
    for (let i = 1; i <= N; i++) {
        dp[i] = [1, 1];
    }
    for (let slip = 0; slip < 3; slip++) {
        for (let i = 1; i <= N; i++) {
            const num = nums[i - 1];
            dp[i][num] = dp[i][1 - num] + dp[i - 1][num];
            dp[i][1 - num] = dp[i - 1][1 - num];

        }
    }
    return dp[N][0] + dp[N][1];
};

