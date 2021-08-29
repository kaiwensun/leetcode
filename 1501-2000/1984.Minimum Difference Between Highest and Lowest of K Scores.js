/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minimumDifference = function(nums, k) {
    nums.sort((a, b) => a - b);
    k--;
    let res = Infinity;
    for (let i = 0; i < nums.length - k; i++) {
        res = Math.min(res, nums[i + k] - nums[i]);
    }
    return res;
};

