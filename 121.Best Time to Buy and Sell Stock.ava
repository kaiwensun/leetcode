/**
 *Result:
 * 200 / 200 test cases passed.
 * Status: Accepted
 * Runtime: 1 ms
 * Your runtime beats 94.05% of javasubmissions
 *Date:
 * 9/2/2016
 */
public class Solution {
    public int maxProfit(int[] prices) {
        int min = Integer.MAX_VALUE;
        int profit = 0;
        for(int e : prices){
            //in practice, Math.min/max methods are slower than ?: operators.
            min = min<e?min:e;//Math.min(min,e);
            profit = profit<e-min?e-min:profit;//Math.max(profit,e-min);
        }
        return profit;
    }
}
