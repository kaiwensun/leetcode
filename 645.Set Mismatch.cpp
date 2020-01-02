class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int missing = 0, dup = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != i + 1) {
                int j = nums[i] - 1;
                if (j == -1) {
                    missing = i + 1;
                }
                else if (nums[j] == nums[i]) {
                    dup = nums[i];
                    missing = i + 1;
                    nums[i] = 0;
                }
                else {
                    int tmp = nums[i]; nums[i] = nums[j]; nums[j] = tmp;
                    i--;
                }
            }
        }
        return vector<int>{dup, missing};
    }
};
