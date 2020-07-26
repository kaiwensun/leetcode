/**
 *Result:
 * 33 / 33 test cases passed.
 * Status: Accepted
 * Runtime: 2 ms
 * Your runtime beats 3.31% of javasubmissions.
 *Date:
 * 9/6/2016
 */
public class Solution {
    public void rotate(int[] nums, int k) {
        if(nums==null || nums.length<=1 || k==0)
            return;
        k = nums.length-(k%nums.length);
        System.out.println(k);
        int g = gcd(nums.length,k);
        for(int i=0;i<g;i++){
            int tmp = nums[i];
            int j=i;
            int stop = (i-k+nums.length)%nums.length;
            while(j!=stop){
                int from = (j+k)%nums.length;
                nums[j] = nums[from];
                j = from;
            }
            nums[j]=tmp;
        }
    }
    private int gcd(int a, int b) {
        if (b != 0)
            return gcd(b, a % b);
        else
            return a;
    }
}
