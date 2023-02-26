function leftRigthDifference(nums: number[]): number[] {
    const prefix = [0];
    for (const num of nums) {
        prefix.push(prefix[prefix.length - 1] + num);
    }
    const sum = prefix[prefix.length - 1];
    return nums.map((_, i) => Math.abs(prefix[i] - (sum - prefix[i + 1])));
};

