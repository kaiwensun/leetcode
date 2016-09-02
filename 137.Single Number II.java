/**
 *Basic idea:
 * Binary Search like the quick sort, but only recursively operate on the side where length%3!=0.
 *Result:
 * 11 / 11 test cases passed.
 * Status: Accepted
 * Runtime: 2 ms
 * Your runtime beats 74.52% of javasubmissions.
 *Date:
 * 9/2/2016
 */
public class Solution {
    private final Random rg = new Random();
    public int singleNumber(int[] nums) {
        int[] lr = new int[]{0,nums.length-1};
        while(lr[0]!=lr[1]){
            singleNumber(nums,lr);
        }
        return nums[lr[0]];
    }
    private void singleNumber(int[] nums,int[] lr){
        int p = lr[0];
        int q = lr[1];
        int r = rg.nextInt(q-p+1)+p;
        
        int pivot = nums[r];
        while(p<=q){
            if(nums[p]<=pivot){
                p++;
            }
            else{
                int tmp = nums[p];
                nums[p] = nums[q];
                nums[q] = tmp;
                q--;
            }
        }
        //p is the index of the first element >pivot
        if((p-lr[0])%3==0){
            lr[0] = p;
        }
        else{
            lr[1]=q;
        }
    }
}
