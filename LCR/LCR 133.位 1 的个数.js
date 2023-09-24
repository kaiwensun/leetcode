/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
    let res = 0;
    while (n) {
        res += 1;
        n &= n - 1;
    }
    return res;
};

