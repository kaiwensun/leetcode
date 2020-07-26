/**
 *Result:
 * 401 / 401 test cases passed.
 * Status: Accepted
 * Runtime: 0 ms
 * Your runtime beats 85.31% of cpp submissions.
 */
class Solution {
public:
    bool isHappy(int n) {
        bool visited[1001] = {false};
        while(n!=1){
            if(n>1000){
                int tmpn = 0;
                while(n!=0){
                    tmpn+=(n%10)*(n%10);
                    n/=10;
                }
                n = tmpn;
            }else{
                if(visited[n]){
                    return false;
                }else{
                    visited[n] = true;
                    int tmpn = 0;
                    while(n!=0){
                        tmpn+=(n%10)*(n%10);
                        n/=10;
                    }
                    n = tmpn;
                }
            }
        }
        return true;
    }
};
