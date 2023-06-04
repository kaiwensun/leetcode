function maximizeSum(nums: number[], k: number): number {
    return Math.max(...nums) * k + k * (k - 1) / 2;
};

