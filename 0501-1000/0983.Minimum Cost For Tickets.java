class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        int[] dp = new int[days.length];
        Arrays.fill(dp, Integer.MAX_VALUE);
        int[] ticketTypes = {1, 7, 30};
        int curCost = 0;
        for (int i = 0; i < days.length; i++) {
            for (int j = 0; j < 3; j++) {
                int range = ticketTypes[j];
                int cost = curCost + costs[j];
                for (int k = i; k < days.length && days[k] - days[i] < range; k++) {
                    dp[k] = Math.min(dp[k], cost);
                }
            }
            curCost = dp[i];
        }
        return curCost;
    }
}
