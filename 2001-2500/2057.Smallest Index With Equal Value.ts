function smallestEqual(nums: number[]): number {
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] == i % 10) {
            return i;
        }
    }
    return -1;
};

