function countSubarrays(nums: number[], minK: number, maxK: number): number {
    if (minK > maxK) return 0;
    let res = 0, start = 0;
    let minInd = -1, maxInd = -1;
    nums.forEach((num, end) => {
        if (num > maxK || num < minK) {
            start = end + 1;
            minInd = maxInd = end;
        }
        if (nums[end] === minK) minInd = end;
        if (nums[end] === maxK) maxInd = end;
        res += Math.min(maxInd, minInd) - start + 1;
    });
    return res;
};

