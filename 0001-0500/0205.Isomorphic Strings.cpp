/**
 *Result:
 * 30 / 30 test cases passed.
 * Status: Accepted
 * Runtime: 19 ms
 * Your runtime beats 59.42% of cpp submissions.
 */
class Solution {
public:
	bool isIsomorphic(string s, string t) {
		unordered_map<char, char> s2t;
		unordered_map<char, char> t2s;
		for (size_t i = 0; i < s.length();i++){
			char cs = s2t[s[i]];
			char ct = t2s[t[i]];
			if (cs == 0 && ct == 0){
				s2t[s[i]] = t[i];
				t2s[t[i]] = s[i];
			}
			else if(s[i]!=ct || t[i]!=cs){
				return false;
			}
		}
		return true;
	}
};
