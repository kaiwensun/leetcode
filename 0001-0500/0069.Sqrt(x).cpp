/**
 *Basic idea:
 * binary search on the root. Becareful about integers greater than (maxroot)^2.
 *Result:
 * 1017 / 1017 test cases passed.
 * Status: Accepted
 * Runtime: 3 ms
 * Your runtime beats 66.95% of cpp submissions.
 *Date:
 * 10/2/2016
 */

class Solution {
public:
    int mySqrt(int x) {
        int l = 0;
        int h = 46340;  //ceil[sqrt((1<<32)-1)]
        if(h*h<=x){
            return h;
        }
        while(l<h){
            int mid = (l+h)/2;
            int sqr = mid*mid;
            if(sqr>x){
                h = mid;
            }else if(sqr<x){
                if(l==mid)
                    return mid;
                l = mid;
            }else{
                return mid;
            }
        }
        return l;
    }
};
