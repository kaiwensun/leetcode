class Solution {
    public int longestSemiRepetitiveSubstring(String s) {
        List<Integer> pivots = new ArrayList<>();
        char prev = s.charAt(0);
        for (int i = 0; i < s.length(); i++) {
            char cur = s.charAt(i);
            if (prev == cur) {
                pivots.add(i);
            }
            prev = cur;
        }
        pivots.add(s.length());
        if (pivots.size() <= 3) {
            return s.length();
        }
        int res = 0;
        for (int i = 0; i < pivots.size() - 2; i++) {
            res = Math.max(res, pivots.get(i + 2) - pivots.get(i));
        }
        return res;
    }
}

