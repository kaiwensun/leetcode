class Solution {
    public int maxRepOpt1(String text) {
        int[] cnt = new int[26];
        for (char c : text.toCharArray()) {
            cnt[c - 'a'] += 1;
        }
        int[] window = new int[3];
        char[] chars = new char[3]; chars[2] = text.charAt(0);
        int res = 0;
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            window[2] += 1;
            if ( i == text.length() - 1 || text.charAt(i + 1) != c) {
                if (chars[0] == chars[2] && window[1] == 1) {
                    res = Math.max(res, window[0] + window[2] + (
                        cnt[chars[2] - 'a'] > window[0] + window[2] ? 1 : 0
                    ));
                } else {
                    res = Math.max(res, window[2] + (
                        cnt[chars[2] - 'a'] > window[2] ? 1 : 0
                    ));
                }
                if (i != text.length() - 1) {
                    window[0] = window[1]; window[1] = window[2]; window[2] = 0;
                    chars[0] = chars[1]; chars[1] = chars[2]; chars[2] = text.charAt(i + 1);
                }
            }
        }
        return res;
    }
}
