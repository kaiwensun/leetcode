class Solution {
    public int balancedStringSplit(String s) {
        int cnt = 0;
        int res = 0;
        for (char c : s.toCharArray()) {
            switch(c) {
                case 'L': cnt ++; break;
                case 'R': cnt --; break;
            }
            if (cnt == 0) {
                res ++;
            }
        }
        return res;
    }
}
