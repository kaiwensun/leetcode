class Solution {
    public boolean checkDistances(String s, int[] distance) {
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int dist = distance[c - 'a'] + 1;
            if (!(i - dist >= 0 && s.charAt(i - dist) == c) && !(i + dist < s.length() && s.charAt(i + dist) == c)) {
                return false;
            }
        }
        return true;
    }
}

