function waysToSplitArray(nums: number[]): number {
    const sum = nums.reduce((acc, num) => acc + num, 0);
    let res = 0,  prefix = 0;
    for (let i = 0; i < nums.length - 1; i++) {
        prefix += nums[i];
        if (prefix >= sum - prefix) {
            res++;
        }
    }
    return res;
};

