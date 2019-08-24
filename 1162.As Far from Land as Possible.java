class Solution {
    int[] DELTA = new int[] {1, 0, -1, 0, 1};
    public int maxDistance(int[][] grid) {
        Queue<int[]> queue = initQueue(grid);
        int res = 1;
        int M = grid.length, N = grid[0].length;
        while (!queue.isEmpty()) {
            int[] next = queue.poll();
            int i = next[0], j = next[1];
            int dist = grid[i][j] == 1 ? -1 : grid[i][j] - 1;
            for (int k = 0; k < 4; k++) {
                int nexti = i + DELTA[k], nextj = j + DELTA[k + 1];
                if (nexti < 0 || nexti >= M || nextj < 0 || nextj >= N || grid[nexti][nextj] != 0) {
                    continue;
                }
                res = Math.min(res, dist);
                grid[nexti][nextj] = dist;
                queue.offer(new int[]{nexti, nextj});
            }
        }
        return -res;
    }
    
    private Queue<int[]> initQueue(int[][] grid) {
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j ++) {
                if (grid[i][j] == 1) {
                    queue.offer(new int[] {i, j});
                }
            }
        }
        return queue;
    }
}
