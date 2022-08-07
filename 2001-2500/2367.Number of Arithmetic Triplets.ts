function arithmeticTriplets(nums: number[], diff: number): number {
    const seen = {};
    let res = 0;
    nums.forEach((num, i) => {
        for (let times = 3; times > 0; times--) {
            const t = times === 1 ? 1 : (seen[[num - diff, times - 1].toString()] || 0);
            if (times === 3) {
                res += t;
            } else {
                seen[[num, times].toString()] = (seen[[num, times].toString()] || 0) + t;
            }
        }
    });
    return res;
};

