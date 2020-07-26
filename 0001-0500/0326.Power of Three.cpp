/**
 *Basic idea:
 * The maximum possible of 3's power has all and only 3's powers as its fractor.
 *Result:
 * 21038 / 21038 test cases passed.
 * Status: Accepted
 * Runtime: 55 ms
 * Your runtime beats 6.37% of cpp submissions.
 *Date:
 * 11/15/2016
 */
class Solution {
public:
    bool isPowerOfThree(int n) {
        return n>0 && 1162261467%n==0;
    }
};
