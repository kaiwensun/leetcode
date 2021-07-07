function numSubarraysWithSum(nums: number[], goal: number): number {
    const seen = { 0: 1 };
    let sum = 0, res = 0;
    for (let num of nums) {
        sum += num;
        res += seen[sum - goal] || 0;
        seen[sum] ||= 0;
        seen[sum]++;
    }
    return res;
};

