class Solution {
public:
    int maxScore(vector<int>& nums) {
        std::sort(nums.begin(), nums.end(), std::greater<>());
        long sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            if (sum <= 0) {
                return i;
            }
        }
        return nums.size();
    }
};

