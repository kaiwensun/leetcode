class Solution {
    public int brokenCalc(int X, int Y) {
        int res = 0;
        while (X < Y) {
            res += 1 + (Y & 1);
            Y = (Y + 1) / 2;
        }
        res += X - Y;
        return res;
    }
}

