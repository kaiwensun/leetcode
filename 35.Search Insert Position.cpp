/**
 *Result:
 * 62 / 62 test cases passed.
 * Status: Accepted
 * Runtime: 6 ms
 * Your runtime beats 26.39% of cpp submissions.
 *Date:
 * 12/12/2016
 */
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size();
        while(l<r){
            int mid = (l+r)/2;
            if(nums[mid]>target){
                r = mid;
            }
            else if(nums[mid]==target){
                return mid;
            }else{
                l = mid+1;
            }
        }
        return l;
    }
};
