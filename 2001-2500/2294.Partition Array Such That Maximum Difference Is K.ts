function partitionArray(nums: number[], k: number): number {
    let start = -Infinity, res = 0;
    for (let num of nums.sort((a, b) => a - b)) {
        if (num > start + k) {
            start = num;
            res++;
        }
    }
    return res;
};

