/**
 * Basic idea:
 * 	bit operation.
 * Result:
 * 	1108 / 1108 test cases passed
 * 	Status: Accepted
 * 	Runtime: 4 ms
 * Date:
 * 	2/6/2016
 */
public class Solution {
    public boolean isPowerOfTwo(int n) {
        //(the rightmost bit 1 is the only one bit 1) and (n is not b1000...0)
        return ((n & -n)==n) && (n<<1!=0);
    }
}

