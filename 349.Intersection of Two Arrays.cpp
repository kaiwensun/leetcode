/**
 *Result:
 * 60 / 60 test cases passed.
 * Status: Accepted
 * Runtime: 13 ms
 * Your runtime beats 33.87% of cpp submissions.
 */
class Solution {
public:
	vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
		unordered_set<int> set1(nums1.begin(),nums1.end());
		unordered_set<int> set2(nums2.begin(), nums2.end());
		vector<int> result;
		for (auto i : set1){
			if (set2.find(i) != set2.end()){
				result.push_back(i);
			}
		}
		return result;
	}
};
