class Solution {
    public int[][] spiralMatrixIII(int R, int C, int r0, int c0) {
        int[][] res = new int[R * C][2];
        int[][] directions = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        res[0] = new int[]{r0, c0};
        int p = 1;
        int dirPtr = 0;
        int edgeSize = 1;
        int i = r0, j = c0;
        while(p < res.length) {
            for (int $ = 0; $ < 2; $++) {
                for (int k = 0; k < edgeSize; k++) {
                    i += directions[dirPtr][0];
                    j += directions[dirPtr][1];
                    System.out.println(i + ", " + j);
                    if (0 <= i && i < R && 0 <= j && j < C) {
                        res[p++] = new int[]{i, j};
                        if (p == res.length) {
                            return res;
                        }
                    }
                }
                dirPtr = (dirPtr + 1) % 4;
            }
            edgeSize++;
        }
        return res;
    }
}

