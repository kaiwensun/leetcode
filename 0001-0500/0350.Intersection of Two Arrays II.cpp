/**
 *61 / 61 test cases passed.
 * Status: Accepted
 * Runtime: 9 ms
 * Your runtime beats 55.47% of cpp submissions.
 */

class Solution {
public:
	vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
		sort(nums1.begin(), nums1.end());
		sort(nums2.begin(), nums2.end());
		vector<int> result;
		vector<int>::iterator i1 = nums1.begin();
		vector<int>::iterator i2 = nums2.begin();
		while (i1 != nums1.end() && i2 != nums2.end()){
			if (*i1 == *i2){
				result.push_back(*i1);
				i1++;
				i2++;
			}
			else if (*i1 < *i2){
				i1++;
			}
			else{
				i2++;
			}
		}
		return result;
	}
};
