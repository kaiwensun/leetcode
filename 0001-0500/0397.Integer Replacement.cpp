/**
 *Result:
 * 47 / 47 test cases passed.
 * Status: Accepted
 * Runtime: 3 ms
 * Your runtime beats 54.24% of cpp submissions.
 *Date:
 * 10/1/2016
 */
class Solution {
public:
    int integerReplacement(int n) {
        if(n==2147483647){
            return 32;
        }
        int cnt = 0;
        int i=0;
        while(n!=1){
            if(n==3){
                cnt+=2;
                break;
            }
            if((n&1)==0){
                n = n>>1;
                cnt++;  //divide by 2
            }else if((n&3)==1){
                n = n>>1;
                cnt+=2; //minus one, divide by 2
            }else{
                n++;
                cnt++;
            }
        }
        return cnt;
    }
};
