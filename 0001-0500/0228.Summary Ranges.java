/**
 * Basic idea:
 * 	mark start and end, traverse correctly.
 * Result:
 * 	27 / 27 test cases passed.
 * 	Status: Accepted
 * 	Runtime: 0 ms
 * Date:
 * 	2/6/2016
 */
 	

public class Solution {
    public List<String> summaryRanges(int[] nums) {
        ArrayList<String> rtn = new ArrayList<String>();
        if(nums.length==0)
            return rtn;
        if(nums.length==1)
        {
            rtn.add(""+nums[0]);
            return rtn;
        }
        int start,end;
        int i=0;
        while(i<nums.length)
        {
            start = nums[i++];
            while(i<nums.length && nums[i]==nums[i-1]+1)i++;
            end = nums[i-1];
            rtn.add(start==end?""+start:start+"->"+end);
        }
        return rtn;
    }
}

