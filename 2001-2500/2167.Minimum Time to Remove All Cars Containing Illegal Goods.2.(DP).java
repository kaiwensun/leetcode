class Solution {
    public int minimumTime(String s) {
        int res = s.length();
        int cur = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                cur = Math.min(i + 1, cur + 2);
            }
            res = Math.min(res, cur + s.length() - 1 - i);
        }
        return res;
    }
}

