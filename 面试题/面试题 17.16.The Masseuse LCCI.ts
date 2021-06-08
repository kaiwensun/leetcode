function massage(nums: number[]): number {
    let dp = [0, 0];  // booked, not booked
    for (let num of nums) {
        dp = [dp[1] + num, Math.max(...dp)];
    }
    return Math.max(...dp);
};

