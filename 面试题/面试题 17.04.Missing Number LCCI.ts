function missingNumber(nums: number[]): number {
    let xor = nums.length;
    for (let i in nums) {
        xor ^= +i ^ nums[i];
    }
    return xor;
}
;
