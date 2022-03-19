function divideArray(nums: number[]): boolean {
    nums.sort();
    for (let i = 0; i < nums.length; i += 2) {
        if (nums[i] !== nums[i + 1]) return false;
    }
    return true;
};

