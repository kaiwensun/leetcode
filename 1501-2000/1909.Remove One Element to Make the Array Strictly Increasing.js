/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canBeIncreasing = function(nums) {
    let violated = false;
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] >= nums[i + 1]) {
            if (violated) return false;
            if (i - 1 >= 0 && nums[i - 1] < nums[i + 1]) {
                nums[i] = nums[i - 1];
            } else if (i + 2 < nums.length && nums[i] < nums[i + 2]) {
                nums[i + 1] = nums[i];
            } else if (i == 0 || i == nums.length - 2) {
                nums[i] = Number.NEGATIVE_INFINITY;
            } else {
                return false;
            }
            violated = true;
        }
    }
    return true;
};

