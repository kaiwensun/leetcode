class Solution {
    public int captureForts(int[] forts) {
        int prevFort = 0, cur = 0, res = 0;
        for (int i = 0; i < forts.length; i++) {
            int fort = forts[i];
            if (fort == 0 && prevFort != 0) {
                cur++;
            } else if (fort == 1 || fort == -1) {
                if (fort == 0 - prevFort) {
                    res = Math.max(res, cur);
                }
                prevFort = fort;
                cur = 0;
            }
        }
        return res;
   }
}

