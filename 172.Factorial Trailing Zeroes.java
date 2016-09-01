/**
 *Basic Idea:
 * How many integers <= n are there having factor 5? The answer is n/5.
 * Then divide all integers <= n by 5 and see how many of them are still dividable by 5.
 * Repeat until n < 5. Do the same thing with factor 2.
 * Return the minimal of count of 5 and 2.
 *Result:
 * 502 / 502 test cases passed.
 * Status: Accepted
 * Runtime: 2 ms
 * Your runtime beats 3.73% of javasubmissions.
 *Date:
 * 9/1/2016
 */ 
public class Solution {
    public int trailingZeroes(int n) {
        return Math.min(countFactor(n,5),countFactor(n,2));
    }
    private int countFactor(int num, int factor){
        int count = 0;
        while(num>=factor){
            num /= factor;
            count += num;
        }
        return count;
    }
}
