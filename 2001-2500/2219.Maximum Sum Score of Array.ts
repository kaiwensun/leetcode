function maximumSumScore(nums: number[]): number {
    const sum = new Array(nums.length);
    let s = 0;
    for (let i = 0; i < nums.length; i++) {
        s += nums[i];
        sum[i] = s;
    }
    s = 0;
    let res = -Infinity;
    for (let i = nums.length - 1; i >= 0; i--) {
        s += nums[i];
        res = Math.max(sum[i], s, res);
    }
    return res;
};

