function findValueOfPartition(nums: number[]): number {
    nums.sort((a, b) => a - b);
    let diff = Infinity;
    for (let i = 1; i < nums.length; i++) {
        diff = Math.min(diff, nums[i] - nums[i - 1]);
    }
    return diff;
};

