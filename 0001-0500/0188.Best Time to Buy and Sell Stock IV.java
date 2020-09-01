class Solution {
    public int maxProfit(int k, int[] prices) {
        
        if (k > prices.length / 2) {
            return quickSolve(prices, prices.length);
        }
        int length = simplifyPrices(prices);
        if (k > prices.length / 2) {
            return quickSolve(prices, length);
        }
        int[] buy = new int[k + 1];
        int[] sell = new int[k + 1];
        Arrays.fill(buy, Integer.MIN_VALUE);
        for (int p = 0; p < length; ++p) {
            for (int i = k; i > 0; --i) {
                sell[i] = Math.max(sell[i], buy[i] + prices[p]);
                buy[i] = Math.max(buy[i], sell[i - 1] - prices[p]);
            }
        }
        return sell[k];
    }
    
    private int simplifyPrices(int[] prices) {
        int simpIndex = 1;
        for (int i = 1; i < prices.length; ++i) {
            int trend = prices[simpIndex] - prices[simpIndex - 1];
            int delta = prices[i] - prices[i - 1];
            if (trend == 0) {
                prices[simpIndex] = prices[i];
            } else if ((trend > 0 && delta < 0) || (trend < 0 && delta > 0)) {
                prices[simpIndex++] = prices[i - 1];
                prices[simpIndex] = prices[i];
            }
        }
        if (simpIndex < prices.length) {
            prices[simpIndex++] = prices[prices.length - 1];
        }
        return simpIndex;
    }
    
    private int quickSolve(int[] prices, int length) {
        int len = length, profit = 0;
            for (int i = 1; i < len; i++)
                if (prices[i] > prices[i - 1])
                    profit += prices[i] - prices[i - 1];
            return profit;
    }
}
