class Solution {
    public long totalCost(int[] costs, int k, int candidates) {
        long res = 0;
        int i = 0, j = costs.length - 1;
        PriorityQueue<Integer> left = new PriorityQueue<>();
        PriorityQueue<Integer> right = new PriorityQueue<>();
        while (i < candidates) {
            left.add(costs[i++]);
        }
        while (j > Math.max(costs.length - 1 - candidates, i - 1)) {
            right.add(costs[j--]);
        }
        while (k-- > 0) {
            int e1 = left.isEmpty() ? Integer.MAX_VALUE : left.peek(), e2 = right.isEmpty() ? Integer.MAX_VALUE : right.peek();
            if (e1 <= e2) {
                left.poll();
                if (i <= j) {
                    left.add(costs[i++]);
                }
                res += e1;
            } else {
                right.poll();
                if (i <= j) {
                    right.add(costs[j--]);
                }
                res += e2;
            }
        }
        return res;
    }
}

