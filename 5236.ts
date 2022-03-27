function minDeletion(nums: number[]): number {
    let res = 0, i = 0;
    while (i < nums.length) {
        while (i + 1 < nums.length && nums[i] === nums[i + 1]) {
            i++;
            res++;
        }
        i += 2;
    }
    if (i !== nums.length) {
        res++;
    }
    return res;
};


