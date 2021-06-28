/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAlternatingSum = function (nums) {
    let res = 0;
    let sm1 = sm2 = 0;
    for (let num of nums) {
        [sm1, sm2] = [Math.max(sm1, sm2 - num, 0), Math.max(sm2, sm1 + num)];
        res = Math.max(res, sm2);
    }
    return res;
};

