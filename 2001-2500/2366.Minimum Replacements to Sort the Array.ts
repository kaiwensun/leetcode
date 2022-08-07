function minimumReplacement(nums: number[]): number {
    let res = 0;
    nums.push(nums[nums.length - 1]);
    for (let i = nums.length - 2; i >= 0; i--) {
        const parts = Math.ceil(nums[i] / nums[i + 1]);
        res += parts - 1;
        nums[i] = Math.floor(nums[i] / parts);
    }
    return res;
};

