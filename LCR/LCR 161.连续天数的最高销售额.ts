function maxSubArray(nums: number[]): number {
    let maxSum = -Infinity, sm = 0;
    nums.forEach(num => {
        sm += num;
        maxSum = Math.max(maxSum, sm);
        sm = Math.max(sm, 0);
    })
    return maxSum;
};

