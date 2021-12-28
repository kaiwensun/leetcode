class Solution {
    public int maxTotalFruits(int[][] fruits, int startPos, int k) {
        return Math.max(
            maxTotalFirstToRight(fruits, startPos, k),
            maxTotalFirstToRight(reverse(fruits), -startPos, k)
        );
    }

    private int maxTotalFirstToRight(int[][] fruits, int startPos, int k) {
        int i = Arrays.binarySearch(fruits, new int[]{startPos, Integer.MAX_VALUE}, (int[] a, int[] b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);
        int startInd = - i - 2;
        int endInd;
        int total = 0;
        for (endInd = startInd; endInd >= 0 && startPos - fruits[endInd][0] <= k; endInd--) {
            total += fruits[endInd][1];
        }
        endInd++;
        int res = total;
        for (int turningInd = startInd + 1; turningInd < fruits.length && fruits[turningInd][0] - startPos <= k; turningInd++) {
            total += fruits[turningInd][1];
            while (fruits[endInd][0] < startPos && fruits[turningInd][0] - startPos + fruits[turningInd][0] - fruits[endInd][0] > k) {
                total -= fruits[endInd++][1];
            }
            res = Math.max(res, total);
        }
        return res;
    }

    private int[][] reverse(int[][] fruits) {
        for (int l = 0, r = fruits.length - 1; l <= r; l++, r--) {
            if (l == r) {
                fruits[l][0] = -fruits[l][0];
            } else {
                int tmp = fruits[l][0]; fruits[l][0] = -fruits[r][0]; fruits[r][0] = -tmp;
                tmp = fruits[l][1]; fruits[l][1] = fruits[r][1]; fruits[r][1] = tmp;
            }
        }
        return fruits;
    }
}

