function largestVariance(s: string): number {
    const N = s.length;
    const charSet = new Set([...s]);
    const dp = new Array(N);
    function largestVarianceForTwo(a: string, b: string) {
        if (a === b) return 0;
        const cnt = {};
        let res = 0;
        cnt[a] = cnt[b] = 0;
        let minDiff = 0, j = 0;
        for (let i = 0; i < N; i++) {
            const c = s[i];
            if (a === c || b === c) {
                cnt[c]++;
            }
            dp[i] = {...cnt};
            if (cnt[a] && cnt[b]) {
                while (dp[j][a] !== cnt[a] && dp[j][b] !== cnt[b]) {
                    minDiff = Math.min(minDiff, dp[j][a] - dp[j][b]);
                    j++;
                }
                res = Math.max(res, cnt[a] - cnt[b] - minDiff);
            }
        }
        return res;
    }
    let res = 0;
    charSet.forEach(a => {
        charSet.forEach(b => {
            res = Math.max(res, largestVarianceForTwo(a, b));
        });
    })
    return res;
};

