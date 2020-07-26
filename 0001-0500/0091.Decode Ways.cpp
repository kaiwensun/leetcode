class Solution {
public:
    int numDecodings(string s) {
        int pre1 = 0, pre2 = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i == 0) {
                pre1 = pre2 = s[i] == '0' ? 0 : 1;
            } else {
                int cur = 0;
                if (s[i - 1] == '1' || (s[i - 1] == '2' && s[i] <= '6')) {
                    cur += pre1;
                }
                if (s[i] != '0'){
                    cur += pre2;
                }
                pre1 = pre2; pre2 = cur;
            }
        }
        return pre2;
    }
};
