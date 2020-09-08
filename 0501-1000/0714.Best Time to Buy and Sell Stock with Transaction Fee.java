class Solution {
    public int maxProfit(int[] prices, int fee) {
        int buy = -100000;
        int sell = 0;
        for (int price : prices) {
            int tmpBuy = buy;
            buy = Math.max(buy, sell - price);
            sell = Math.max(sell, tmpBuy + price - fee);
        }
        return sell;
    }
}

