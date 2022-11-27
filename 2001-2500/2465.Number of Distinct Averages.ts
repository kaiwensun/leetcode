function distinctAverages(nums: number[]): number {
    const set = new Set();
    nums.sort((a, b) => a - b);
    for (let i = 0; i < nums.length / 2; i++) {
        set.add(nums[i] + nums[nums.length - 1 - i]);
    }
    return set.size;
};

