class Solution {
    public int minimumSum(int n, int k) {
        Set<Integer> seen = new HashSet<>();
        for (int i = 1; seen.size() < n; i++) {
            if (!seen.contains(k - i)) {
                seen.add(i);
            }
        }
        return seen.stream().reduce(0, (a, b) -> a + b);
    }
}

