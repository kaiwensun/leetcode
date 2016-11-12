/**
 *Basic idea:
 * binary search on the number of rows.
 *Result:
 * 1336 / 1336 test cases passed.
 * Status: Accepted
 * Runtime: 9 ms
 * Your runtime beats 63.04% of cpp submissions.
 */
class Solution {
public:
    int arrangeCoins(int n) {
        if(n>2147450880){
            return 65535;
        }
        unsigned int m = n;
        unsigned int l = 0;
        unsigned int r = 65535;
        while(l<r){
            unsigned int mid = (l+r+1)/2;
            unsigned cnt = mid*(mid+1)/2;
            if(cnt>n){
                r = mid-1;
            }else{
                l = mid;
            }
        }
        return l;
    }
};
