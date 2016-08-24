/**
 * Basic Idea:
 *  Record a 'first' and 'second' which indicate a length-2 increasing subsequence we've found so far.
 *  Record a 'min' which indicates the smallest number in the array, but the min might not be in a length-2 increasing subsequence.
 *  Traverse the array and update those records, until we reach the end or find a number greater than 'second'.
 * Improved Idea:
 *  We don't need the 'first'. Since a third number in the increasing subsequence is greater than 'second',
 *  it is of course greater than some 'first' which appears before 'second'.
 * Result:
 *  61 / 61 test cases passed.
 *  Status: Accepted
 *  Runtime: 1 ms
 *  Your runtime beats 40.56% of javasubmissions
 * Date:
 *  8/24/2016
 */
public class Solution {
    public boolean increasingTriplet(int[] nums) {
        if(nums==null || nums.length<3)
            return false;
        int first = nums[0];
        int second = Integer.MAX_VALUE;
        int min = nums[0];
        for(int num : nums){
            //System.out.println("BEFORE: num="+num+", first="+first+",second="+second+",min="+min);
            if(num<min){
                min = num;
            }
            else if(num>min && num<=first){
                first = min;
                second = num;
            }
            else if(num>first && num<second){
                second = num;
            }
            else if(num>second){
                return true;
            }
            //System.out.println("AFTER: num="+num+", first="+first+",second="+second+",min="+min);
            
        }
        return false;
    }
}
