/**
 *Result:
 * 25 / 25 test cases passed.
 * Status: Accepted
 * Runtime: 0 ms
 * Your runtime beats 4.57% of cpp submissions.
 *Date:
 * 10/17/2016
 */

// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int l = 1;
        int r = n;
        while(l<r){
            int mid = l+(r-l)/2;    //avoid overflow
            int res = guess(mid);
            if(res==0)
                return mid;
            else if(res==1){
                l = mid+1;
            }else{
                r = mid-1;
            }
        }
        return l;
    }
};
