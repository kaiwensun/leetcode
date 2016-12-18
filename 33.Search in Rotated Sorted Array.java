public class Solution {
    public int search(int[] nums, int target) {
        if(nums==null || nums.length==0)
            return -1;
        int l = 0;
        int r = nums.length-1;
        while(l<r){
            int mid = (l+r)/2;
            if(nums[l]<nums[r]){
                if(target<nums[l] || target>nums[r]){
                    return -1;
                }
                if(nums[mid]<target){
                    l = mid+1;
                }else if(nums[mid]==target){
                    return mid;
                }else{
                    r = mid-1;
                }
            }else{
                if(target>=nums[l]){
                    if(nums[mid]<nums[r]){
                        r = mid-1;
                    }else{
                        if(nums[mid]<target){
                            l = mid+1;
                        }else if(nums[mid]==target){
                            return mid;
                        }else{
                            r = mid-1;
                        }
                    }
                }else if(target<=nums[r]){
                    if(nums[mid]<nums[r]){
                        if(nums[mid]<target){
                            l = mid+1;
                        }else if(nums[mid]==target){
                            return mid;
                        }else{
                            r = mid-1;
                        }
                    }else{
                        l  = mid+1;
                    }
                }else{
                    return -1;
                }
            }
        }
        if(nums[l]==target){
            return l;
        }else if(r>=0 && nums[r]==target){
            return r;
        }else{
            return -1;
        }
            
    }
}
