/**
 * Basic idea:
 *  Greedy. The problem is equivalent to looking for the number of "change points"
 *  in the whole sequence, where "change point" is where the sequence switch
 *  increasing/decreasing, or a terminal of the sequence. Proof: suppose at some
 *  point where A<B<C, we thought A and B are (temporarily) in the subsequence and
 *  want to decide whether we should replace B with C. Greedily replace B with C
 *  will not leads to a shorter subsequence, because for any subsequence not replacing
 *  B with C, B's next element is less than B (and thus less than C), so we can let it
 *  be C's next element and keeps all other unaffected elements in the subsequence unchanged.
 *  Then the newly constructed subsequence replacing B with C has exactly same length as
 *  the old subsequence. So greedy algo doesn't lead to a worse result. It works!
 * Result:
 *  23 / 23 test cases passed.
 *  Status: Accepted
 *  Runtime: 0 ms
 *  Your runtime beats 56.36% of javasubmissions.
 * Date:
 *  8/16/2016
 */
public class Solution {
    public int wiggleMaxLength(int[] nums) {
        if(nums==null)
            return 0;
        if(nums.length<2)
            return nums.length;
        int start = 0;
        while(true){
            if(nums[start]!=nums[start+1])
                break;
            start++;
            if(start==nums.length-1)
                return 1;
        }
        int cnt = 2;
        boolean increasing = (nums[start]<nums[start+1]);
        for(int i=start;i<nums.length-1;i++){
            if(nums[i]==nums[i+1])
                continue;
            if((nums[i]<nums[i+1]) ^ increasing){
                cnt++;
                increasing = !increasing;
            }
        }
        return cnt;
    }
}
