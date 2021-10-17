function countMaxOrSubsets(nums: number[]): number {
    let target = 0, res = 0;
    for (let num of nums) {
        target |= num;
    }
    const dfs = (i: number, bits: number) => {
        if (i === nums.length) {
            if (bits === target) {
                res++;
            }
            return;
        }
        dfs(i + 1, bits);
        dfs(i + 1, bits | nums[i]);
    }
    dfs(0, 0);
    return res;
};

