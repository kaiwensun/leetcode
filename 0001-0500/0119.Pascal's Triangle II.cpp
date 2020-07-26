/**
 *Result:
 * 34 / 34 test cases passed.
 * Status: Accepted
 * Runtime: 0 ms
 * Your runtime beats 37.43% of cpp submissions.
 */
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> res;
        for(int i=0;i<=rowIndex;i++){
            int old =  1;
            for(int j=1;j<i;j++){
                int tmp = res[j];
                res[j] = old + res[j];
                old = tmp;
            }
            res.push_back(1);
        }
        return res;
    }
};
