class Solution {
    public int[] divisibilityArray(String word, int m) {
        long cur = 0;
        int[] res = new int[word.length()];
        char zero = '0';
        for (int i = 0; i < word.length(); i++) {
            int d = word.charAt(i) - zero;
            cur *= 10;
            cur += d;
            cur %= m;
            res[i] = cur == 0 ? 1 : 0;
        }
        return res;
    }
}

