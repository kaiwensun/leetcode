function zeroFilledSubarray(nums: number[]): number {
    nums.push(-1);
    let acc = 0, res = 0;
    for (const num of nums) {
        if (num) {
            res += (1 + acc) * acc / 2;
            acc = 0;
        } else {
            acc++;
        }
    }
    return res;
};

