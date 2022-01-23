function findLonely(nums: number[]): number[] {
    const counter = {};
    for (const num of nums) {
        counter[num] ||= 0;
        counter[num]++;
    }
    return nums.filter(num => counter[num] === 1 && !counter[num - 1] && !counter[num + 1]);
};

