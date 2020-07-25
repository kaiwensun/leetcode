class Solution {
    public int minNumberOperations(int[] target) {
        int left = 0, res = 0;
        for (int num : target) {
            res += Math.max(left - num, 0);
            left = num;
        }
        res += left;
        return res;
    }
}
