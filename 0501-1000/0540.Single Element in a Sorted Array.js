/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function(nums) {
    var lo = 0, hi = (nums.length - 1) / 2;
    while (lo < hi) {
        var mid = Math.floor((lo + hi) / 2);
        if (nums[mid * 2] == nums[mid * 2 + 1]) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return nums[hi * 2];
};
