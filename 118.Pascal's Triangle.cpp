/**
 *Result:
 * 15 / 15 test cases passed.
 * Status: Accepted
 * Runtime: 3 ms
 * Your runtime beats 1.06% of cpp submissions.
 */
class Solution {
public:
	vector<vector<int>> generate(int numRows) {
		vector<vector<int>> res;
		if (numRows <= 0){
			return res;
		}
		res.push_back(vector<int>{1});
		for (int i = 1; i < numRows; i++){
			vector<int>row{ 1 };
			for (int j = 1; j < i; j++){
				row.push_back(res.at(i - 1).at(j - 1) + res.at(i - 1).at(j));
			}
			row.push_back(1);
			res.push_back(row);
		}
		return res;
	}
};
