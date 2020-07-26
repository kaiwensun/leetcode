/**
 *Result:
 * 15 / 15 test cases passed.
 * Status: Accepted
 * Runtime: 1 ms
 * Your runtime beats 40.13% of java submissions.
 *Date:
 * 10/27/2016
 */
public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length-1;
        while(l<r){
            int sum = numbers[l]+numbers[r];
            if(sum>target){
                r--;
            }else if(sum<target){
                l++;
            }else{
                return new int[] {l+1,r+1};
            }
        }
        return null;
    }
}
