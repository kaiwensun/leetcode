function findPrefixScore(nums: number[]): number[] {
    const ans: number[] = [];
    let prefix_sum = 0;
    let maxprefix_sum = 0;
    let max = 0;
    for (const num of nums) {
        prefix_sum += num;
        max = Math.max(max, num);
        maxprefix_sum += max;
        ans.push(prefix_sum + maxprefix_sum);
    }
    return ans;
};

