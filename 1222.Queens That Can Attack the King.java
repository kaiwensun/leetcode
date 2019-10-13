class Solution {
    public List<List<Integer>> queensAttacktheKing(int[][] queens, int[] king) {
        List<List<Integer>> res = new LinkedList<>();
        Set<List<Integer>> queensSet = new HashSet<List<Integer>>();
        for (int[] queen : queens) {
            queensSet.add(Arrays.asList(queen[0], queen[1]));
        }
        
        for (int deltax : new int[]{1, 0, -1}) {
            for (int deltay : new int[]{1, 0, -1}) {
                if (deltax == 0 && deltay == 0) {
                    continue;
                }
                int x = king[0] + deltax;
                int y = king[1] + deltay;
                while (0 <= x && x < 8 && 0 <= y && y < 8) {
                    if (queensSet.contains(Arrays.asList(x, y))) {
                        res.add(Arrays.asList(x, y));
                        break;
                    }
                    x += deltax;
                    y += deltay;
                }
            }
        }
        return res;
    }
}
