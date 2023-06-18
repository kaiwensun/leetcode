class Solution {
    public int distanceTraveled(int mainTank, int additionalTank) {
        int res = 0;
        while (mainTank != 0) {
            if (mainTank < 5) {
                res += mainTank;
                break;
            }
            int move = Math.min(mainTank / 5, additionalTank);
            additionalTank -= move;
            res += mainTank / 5 * 5;
            mainTank %= 5;
            mainTank += move;
        }
        return res * 10;
    }
}

