function minimumAverageDifference(nums: number[]): number {
    for (let i = 1; i < nums.length; i++) {
        nums[i] += nums[i - 1];
    }
    let res = undefined, minDiff = Infinity;
    for (let i = 0; i < nums.length; i++) {
        const diff = Math.abs(
            Math.floor(nums[i] / (i + 1)) -
            Math.floor((nums[nums.length - 1] - nums[i]) / Math.max((nums.length - i - 1), 1))
        );
        if (diff < minDiff) {
            minDiff = diff;
            res = i;
        }
    }
    return res;
};

