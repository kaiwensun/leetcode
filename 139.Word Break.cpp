/**
 *Result:
 * 34 / 34 test cases passed.
 * Status: Accepted
 * Runtime: 6 ms
 * Your runtime beats 65.85% of cpp submissions.
 *Date:
 * 12/11/2016
 */
class Solution {
public:
	bool wordBreak(string s, unordered_set<string>& wordDict) {
		bool* dp = new bool[s.length()];
		memset(dp, false, sizeof(bool)*s.length());
		preprocessDict(s, wordDict);
		for (size_t i = 0; i < s.length(); i++){
			for (string str : wordDict){
				if (i >= str.length()-1 && ((i>=str.length() && dp[i - str.length()])||i == str.length()-1) && str == s.substr(i - str.length() + 1, str.length())){
					dp[i] = true;
					break;
				}
			}
		}
		return dp[s.length() - 1];
	}
private:
	void preprocessDict(string& s, unordered_set<string>& wordDict){
		unordered_set<string> cpy = unordered_set<string>(wordDict);
		for (string str : cpy){
			if (str.length() > s.length()){
				wordDict.erase(str);
			}
		}
	}
};
