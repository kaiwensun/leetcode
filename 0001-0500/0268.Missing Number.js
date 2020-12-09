/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let bits = 0;
    for (let i = 0; i < nums.length; i++) {
        bits ^= i ^ nums[i];
    }
    return bits ^ nums.length;
};

