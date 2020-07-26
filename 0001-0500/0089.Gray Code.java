/**
 *Result:
 * 12 / 12 test cases passed.
 * Status: Accepted
 * Runtime: 1 ms
 * We are in the progress of updating the graph distribution. Please check the distribution again within weeks.
 *Date:
 * 9/9/2016
 */
public class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> res = new ArrayList<Integer>(1<<n);
        res.add(0);
        for(int mask = 1;mask<(1<<n);mask = mask<<1){
            for(int i=mask-1;i>=0;i--){
                res.add(res.get(i)|mask);
            }
        }
        return res;
    }
}
