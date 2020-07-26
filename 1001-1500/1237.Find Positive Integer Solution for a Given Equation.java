/*
 * // This is the custom function interface.
 * // You should not implement it, or speculate about its implementation
 * class CustomFunction {
 *     // Returns f(x, y) for any given positive integers x and y.
 *     // Note that f(x, y) is increasing with respect to both x and y.
 *     // i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
 *     public int f(int x, int y);
 * };
 */
class Solution {
    private CustomFunction cf;
    private List<List<Integer>> res;
    
    public List<List<Integer>> findSolution(CustomFunction customfunction, int z) {
        cf = customfunction;
        res = new LinkedList<>();
        int nextY = 1000;
        for (int x = 1; x <= 1000; x++) {
            nextY = searchYForXIs(x, nextY, z);
            nextY = Math.min(nextY, 1000);
            if (nextY == 0) {
                break;
            }
        }
        
        return res;
    }

    private int searchYForXIs(int x, int y, int z) {
        for (; y > 0; y--) {
            int f = cf.f(x, y);
            if (f == z) {
                res.add(Arrays.asList(x, y));
                return y - 1;
            }
            if (f < z) {
                return y + 1;
            }
        }
        return y;
    }
}
