/**
 *Basic idea:
 * use an array to store the minimum value of each length-i increasing subsequence.
 * traverse the original nums array. for every num in nums array, the num can ALWAYS
 * be a new minimal end of some increasing subsequence so far.
 *Result:
 * 24 / 24 test cases passed.
 * Status: Accepted
 * Runtime: 1 ms
 * Your runtime beats 87.08% of java submissions.
 *Date:
 * 10/30/2016
 */

public class Solution {
    public int lengthOfLIS(int[] nums) {
        if(nums==null || nums.length==0){
            return 0;
        }
        int[] minOfTrails = new int[nums.length+2];
        Arrays.fill(minOfTrails,Integer.MAX_VALUE);
        minOfTrails[0] = Integer.MIN_VALUE;
        for(int i=0;i<nums.length;i++){
            int id = idOfFirstGreater(minOfTrails, i+2,nums[i]);
            minOfTrails[id] = nums[i];
        }
        //printArr(minOfTrails);
        return idOfFirstGreater(minOfTrails,nums.length+2,Integer.MAX_VALUE)-1;
    }
    
    private void printArr(int[] arr){
        System.out.print("[");
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]);
            if(i<arr.length-1){
                System.out.print(",");
            }
        }
        System.out.println("]");
    }
    int idOfFirstGreater(int[] array, int arr_len, int value){
        //array is increasingly sorted
        //find the index of the leftmost value which is greater than or equal to the value.
        int l = 0;
        int r = arr_len-1;
        while(l<r){
            int mid = (l+r)/2;
            if(array[mid]<value){
                l = mid+1;
            }else{
                r = mid;
            }
        }
        return l;
   }
}
