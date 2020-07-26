/**
 *Result:
 * 26 / 26 test cases passed.
 * Status: Accepted
 * Runtime: 6 ms
 * Your runtime beats 57.67% of cpp submissions.
 *Date:
 * 11/17/2016
 */
class Solution {
public:
    int thirdMax(vector<int>& nums) {
        int res = INT_MAX;
        for(int i=0;i<3;i++){
            int m = INT_MIN;
            bool changed = false;
            for(int j=0;j<nums.size();j++){
                if(nums[j]==INT_MIN && INT_MIN<res){changed = true;}
                if(nums[j]>m && nums[j]<res){m = nums[j];changed = true;}
            }
            if(!changed){
                res = INT_MIN;
                for(auto n:nums){
                    res = res>n?res:n;
                }
                break;
            }else{
                res = m;
            }
        }
        return res;
    }
};
