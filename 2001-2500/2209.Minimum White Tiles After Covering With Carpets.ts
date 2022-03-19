function minimumWhiteTiles(floor: string, numCarpets: number, carpetLen: number): number {
    const prefix = [0];
    [].forEach.call(floor, c => prefix.push(prefix[prefix.length - 1] + parseInt(c)));
    const range = (start, end) => prefix[Math.min(prefix.length - 1, end)] - prefix[Math.max(0, start)];
    const dp = new Array(floor.length).fill(0);
    for (let i = 0; i < numCarpets; i++) {
        for (let start = 0; start < floor.length; start++) {
            const end = start + carpetLen;
            dp[start] = range(start, end) + (end >= dp.length ? 0 : dp[end]);
        }
        for (let start = floor.length - 2; start >= 0; start--) {
            dp[start] = Math.max(dp[start + 1], dp[start]);
        }
    }
    return prefix[prefix.length - 1] - Math.max(...dp);
};

