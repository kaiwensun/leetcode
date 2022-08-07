function countBadPairs(nums: number[]): number {
    const diff: {[key : number]: number} = {};
    let good = 0;
    nums.forEach((num, i) => {
        good += diff[num - i] ||= 0;
        diff[num - i]++;
    });
    const N = nums.length;
    return N * (N - 1) / 2 - good;
};

