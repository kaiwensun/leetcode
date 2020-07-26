class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int res = 0;
        for (auto i = g.begin(), j = s.begin(); i != g.end() && j != s.end(); j++) {
            if (*i <= *j) {
                res ++;
                i++;
            }
        }
        return res;
    }
};
