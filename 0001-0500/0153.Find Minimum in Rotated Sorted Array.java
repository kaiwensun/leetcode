/**
 *Basic idea:
 * Binary search.
 *Result:
 * 146 / 146 test cases passed.
 * Status: Accepted
 * Runtime: 0 ms
 * Your runtime beats 58.88% of java submissions.
 *Date:
 * 10/29/2016
 */
public class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length-1;
        while(l<r){
            int mid = (l+r)/2;
            if(nums[l]<nums[r]){
                return nums[l];
            }else{//nums[l]>nums[r]
                if(nums[mid]>nums[l]){
                    l = mid+1;
                }else if(nums[mid]<nums[l]){
                    r = mid;
                }else{
                    return nums[l]>nums[r]?nums[r]:nums[l];
                }
            }
        }
        return nums[l]>nums[r]?nums[r]:nums[l];
    }
}
