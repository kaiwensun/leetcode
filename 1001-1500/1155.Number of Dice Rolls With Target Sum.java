class Solution {
    final private static int MOD = 1000000007;
    public int numRollsToTarget(int D, int F, int target) {
        int[] ways = new int[1001];
        int[] newWays = new int[1001];
        ways[0] = 1;
        for (int d = 1; d <= D; d++) {
            for (int f = 1; f <= F; f++) {
                for (int oldWay = 0; oldWay + f <= 1000; oldWay++) {
                    newWays[f + oldWay] += ways[oldWay];
                    newWays[f + oldWay] %= MOD;
                }
            }
            int[] tmp = ways; ways = newWays; newWays = tmp;
            Arrays.fill(newWays, 0);
        }
        return ways[target];
    }
}
