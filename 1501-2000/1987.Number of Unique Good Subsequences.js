/**
 * @param {string} binary
 * @return {number}
 */

 const MOD = 1e9 + 7;

var numberOfUniqueGoodSubsequences = function(binary) {
    let tail0 = 0, tail1 = 0;
    for (const bit of binary) {
        if (bit === '0') {
            tail0 += tail1;
            tail0 %= MOD;
        } else {
            tail1 += tail0 + 1;
            tail1 %= MOD
        }
    }
    return (tail0 + tail1 + (binary.includes('0') ? 1 : 0)) % MOD;
};

