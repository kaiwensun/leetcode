function maxSubsequence(nums: number[], k: number): number[] {
    return nums.map((num, i) => [num, i]).sort((a, b) => b[0] - a[0]).slice(0, k).sort((a, b) => a[1] - b[1]).map(([num, i]) => num);
};

