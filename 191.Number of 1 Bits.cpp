/**
 *Result:
 * 600 / 600 test cases passed.
 * Status: Accepted
 * Runtime: 3 ms
 * Your runtime beats 26.06% of cpp submissions.
 */
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int cnt = 0;
        while(n){
            cnt++;
            n &= n-1;
        }
        return cnt;
    }
};
