/*
 * Basic idea:
 * 	Dynamic programming (compute and store)
 * Result:
 * 	45 / 45 test cases passed.
 * 	Status: Accepted
 * 	Runtime: 0 ms
 * Another idea:
 * 	if O(n) space is not allowed, note that every time we only need previous two steps, and can forget history.
 */
public class Solution {
    public int climbStairs(int n) {
        if(n<=2)
            return n;
        int[] steps = new int[n];
        steps[0]=1;
        steps[1]=2;
        for(int i=2;i<n;i++)
            steps[i] = steps[i-1]+steps[i-2];
        return steps[n-1];
    }
}

