class Solution {
    private int[][] rects;
    private Random rand = new Random();
    public Solution(int[][] rects) {
        this.rects = rects;
    }
    
    public int[] pick() {
        int sm = 0;
        int[] res = null;
        for (int[] rect : rects) {
            int area = (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1);
            sm += area;
            if (rand.nextInt(sm) < area) {
                res = new int[] {rand.nextInt(rect[2] - rect[0] + 1) + rect[0], rand.nextInt(rect[3] - rect[1] + 1) + rect[1]};
            }
        }
        return res;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(rects);
 * int[] param_1 = obj.pick();
 */
