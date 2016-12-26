class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.size()==0){
            return 0;
        }
        int maxSum = nums[0];
        int curSum = 0;
        for(int i=0;i<nums.size();i++){
            curSum += nums[i];
            maxSum = curSum>maxSum?curSum:maxSum;
            curSum = curSum<0?0:curSum;
        }
        return maxSum;
    }
};
