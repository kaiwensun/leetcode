/**
 * @param {number[]} nums
 * @return {number}
 */
var findMiddleIndex = function (nums) {
    let l = 0;
    let r = nums.reduce((acc, num) => acc + num, 0);
    for (let i in nums) {
        r -= nums[i];
        if (l === r) return i;
        l += nums[i];
        
    }
    return -1;
};

