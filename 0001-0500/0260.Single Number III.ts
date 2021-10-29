function singleNumber(nums: number[]): number[] {
    const xor = nums.reduce((xor, num) => xor ^ num);
    const bit = xor & -xor;
    return nums.reduce((xors, num) => [xors[0] ^ (num & bit ? num : 0), xors[1] ^ (num & bit ? 0 : num)], [0, 0]);
};

