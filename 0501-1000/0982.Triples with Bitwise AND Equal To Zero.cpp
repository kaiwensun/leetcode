class Solution {
public:
    int countTriplets(vector<int>& A) {
        int mx = *(max_element(A.begin(), A.end()));
        vector<int> map(mx + 1, 0);
        int res = 0;
        for (int a : A) {
            for (int b : A) {
                map[a & b]++;
            }
        }
        for (int a : A) {
            for (int b = 0; b <= mx; b++) {
                if ((a & b) == 0) {
                    res += map[b];
                }
            }
        }
        return res;
    }
};

