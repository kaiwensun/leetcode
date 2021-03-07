class Solution {
    public int nearestValidPoint(int x, int y, int[][] points) {
        int dist = Integer.MAX_VALUE;
        int res = -1;
        for (int i = 0; i < points.length; i++) {
            int[] point = points[i];
            if (x == point[0] || y == point[1]) {
                int newDist = Math.abs(point[0] - x + point[1] - y);
                if (newDist < dist) {
                    res = i;
                    dist = newDist;
                }
            }
        }
        return res;
    }
}

