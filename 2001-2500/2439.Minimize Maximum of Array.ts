function minimizeArrayValue(nums: number[]): number {
    let res = 0, sum = 0;
    nums.forEach((num, i) => {
        sum += num;
        res = Math.max(res, Math.ceil(sum / (i + 1)));
    });
    return res;
};

