class Solution {
    public int minIncrements(int n, int[] cost) {
        return countIncrements(1, cost)[1];
    }

    private int[] countIncrements(int label, int[] cost) {
        if (label >= cost.length + 1) {
            return new int[]{0, 0};
        }
        int[] left = countIncrements(label * 2, cost);
        int[] right = countIncrements(label * 2 + 1, cost);
        int pathSum = Math.max(left[0], right[0]) + cost[label - 1];
        int newInc = Math.abs(left[0] - right[0]);
        int totalInc = left[1] + right[1] + newInc;
        return new int[]{pathSum, totalInc};
    }
}

