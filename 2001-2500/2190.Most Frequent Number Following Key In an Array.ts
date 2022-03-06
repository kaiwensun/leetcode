function mostFrequent(nums: number[], key: number): number {
    const cnt = {undefined: 0};
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] === key) {
            cnt[nums[i + 1]] ||= 0;
            cnt[nums[i + 1]]++;
        }
    }
    let num = undefined, max = 0;
    Object.entries(cnt).forEach(([key, value]) => {
        if (value > max) {
            num = key;
            max = value;
        }
    });
    return num;
};

