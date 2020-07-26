/**
 *Result:
 * 95 / 95 test cases passed.
 * Status: Accepted
 * Runtime: 3 ms
 * Your runtime beats 62.88% of cpp submissions.
 */
class Solution {
public:
	int longestPalindrome(string s) {
		int cnts['z'-'A'+1] = { 0 };
		for (auto c : s){
			cnts[c - 'A']++;
		}
		int hasSingle = 0;
		int sum = 0;
		for (auto cnt : cnts){
			hasSingle |=(cnt & 1);
			sum += cnt&(-2);
		}
		return sum + hasSingle;
	}
};
