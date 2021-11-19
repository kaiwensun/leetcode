function findLHS(nums: number[]): number {
    let res = 0;
    const cnt = {};
    for (const num of nums) {
        cnt[num] ||= 0;
        cnt[num]++;
        if (cnt[num - 1]) {
            res = Math.max(res, cnt[num] + cnt[num - 1]);
        }
        if (cnt[num + 1]) {
            res = Math.max(res, cnt[num] + cnt[num + 1]);
        }
    }
    return res;
};

