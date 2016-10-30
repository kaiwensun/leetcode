/**
 *Result:
 * 191 / 191 test cases passed.
 * Status: Accepted
 * Runtime: 1 ms
 * Your runtime beats 7.74% of java submissions.
 *Date:
 * 10/29/2016
 */
public class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length-1;
        while(l<r){
            if(nums[l]<nums[r]){
                return nums[l];
            }else if(nums[l]>nums[r]){
                int mid = (l+r)/2;
                /*
                if(nums[mid]>nums[l]){
                    l = mid+1;
                }else if(nums[mid]==nums[l]){
                    l = mid+1;
                }else if(nums[mid]>nums[r]){
                    l = mid+1;
                }else if(nums[mid]==nums[r]){
                    r = mid;
                }else{
                    r = mid;
                }
                */
                if(nums[mid]>nums[r]){
                    l = mid+1;
                }else{
                    r = mid;
                }
            }else{
                //nums[l]==nums[r]
                r--;
            }
        }
        return nums[l];
    }
}
