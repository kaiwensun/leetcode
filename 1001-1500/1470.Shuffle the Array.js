/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    for (var i = 0; i < nums.length; i++) {
        var j = i;
        var buffer = nums[i];
        while (buffer >= 0) {
            j = j < n ? j * 2 : (j - n) * 2 + 1;
            var tmp = buffer; buffer = nums[j]; nums[j] = -tmp;
        }
    }
    for (var i = 0; i < nums.length; i++) {
        nums[i] *= -1;
    }
    return nums;
};

