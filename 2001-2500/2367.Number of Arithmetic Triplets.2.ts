function arithmeticTriplets(nums: number[], diff: number): number {
    const seen = {};
    let res = 0;
    nums.forEach(num => {
        res += seen[num - diff] && seen[num - diff * 2] || 0;
        seen[num] = 1;
    });
    return res;
};

