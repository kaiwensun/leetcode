class Solution {
    public int getMaximumConsecutive(int[] coins) {
        Arrays.sort(coins);
        int res = 0;
        for (int coin : coins) {
            if (coin > res + 1) break;
            res += coin;
        }
        return res + 1;
    }
}

