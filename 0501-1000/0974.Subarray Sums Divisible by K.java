class Solution {
    public int subarraysDivByK(int[] A, int K) {
        Map <Integer, Integer> residualCounter = new HashMap<>();
        residualCounter.put(0, 1);
        int sum = 0;
        for (int a : A) {
            sum += a;
            int residual = Math.floorMod(sum, K);
            residualCounter.put(residual, residualCounter.getOrDefault(residual, 0) + 1);
        }
        int res = 0;
        for (int count : residualCounter.values()) {
            res += count * (count - 1) / 2;
        }
        return res;
    }
}

