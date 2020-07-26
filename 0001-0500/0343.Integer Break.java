/**
 *Result:
 * 50 / 50 test cases passed.
 * Status: Accepted
 * Runtime: 0 ms
 * Your runtime beats 39.81% of javasubmissions.
 *Date:
 * 8/29/2016
 *Another Solution:
 * https://discuss.leetcode.com/topic/43055/why-factor-2-or-3-the-math-behind-this-problem
 */

/*
public class Test{
	public static void main(String[] argv){
		int[] dp = new int[59];
		dp[0] = 1;
		dp[1] = 1;
		for(int num = 2;num<=58;num++){
			int max = -1;
			for(int first = 1;first<num;first++){
				int prod = Math.max(dp[first],first)*Math.max(dp[num-first],num-first);
				max = Math.max(max, prod);
			}
			dp[num] = max;
			System.out.print(max+", ");
		}
	}
	
}
*/
public class Solution {
    private static int[] table = {1, 1, 1, 2, 4, 6, 9, 12, 18, 27, 36, 54, 81, 108, 162, 243, 324, 486, 729, 972, 1458, 2187, 2916, 4374, 6561, 8748, 13122, 19683, 26244, 39366, 59049, 78732, 118098, 177147, 236196, 354294, 531441, 708588, 1062882, 1594323, 2125764, 3188646, 4782969, 6377292, 9565938, 14348907, 19131876, 28697814, 43046721, 57395628, 86093442, 129140163, 172186884, 258280326, 387420489, 516560652, 774840978, 1162261467, 1549681956};
    public int integerBreak(int n) {
        return table[n];
    }
}
