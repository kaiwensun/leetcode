/**
 *Basic idea:
 * binary search
 *Result:
 * 81 / 81 test cases passed.
 * Status: Accepted
 * Runtime: 0 ms
 * Your runtime beats 67.48% of javasubmissions.
 *Date:
 * 9/6/2016
 */
public class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] res = {-1,-1};
        int l = 0;
        int r = nums.length-1;
        if (nums.length == 0) {
            return new int[]{-1, -1};
        }
        if(nums[0]==target)
            res[0] = 0;
        if(nums[nums.length-1]==target)
            res[1] = nums.length-1;
        while(l<=r){
            int mid = (l+r)/2;
            if(nums[mid]<target)
                l = mid+1;
            else if(nums[mid]>target)
                r = mid-1;
            else{
                if(res[0]==-1){
                    int lr = mid;
                    while(l<lr){
                        int lm = (l+lr)/2;
                        if(nums[lm]<target)
                            l = lm+1;
                        else
                            lr = lm;
                    }
                    res[0] = l;
                }
                if(res[1]==-1){
                    int rl = mid;
                    while(rl<r){
                        int rm = (rl+r+1)/2;
                        if(nums[rm]>target)
                            r = rm-1;
                        else
                            rl = rm;
                    }
                    res[1] = r;
                }
                break;
            }
        }
        return res;
    }
}
