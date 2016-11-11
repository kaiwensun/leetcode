/**
 *Result:
 * 84 / 84 test cases passed.
 * Status: Accepted
 * Runtime: 82 ms
 * Sorry. We do not have enough accepted submissions.
 */
#include<algorithm>
class Solution {
public:
	int minMoves(vector<int>& nums) {
		int m = *std::min_element(nums.begin(),nums.end());
		int sum = 0;
		for (auto ele : nums)
			sum += ele - m;
		return sum;
	}
};
