class Solution {
    public int countCharacters(String[] words, String chars) {
        int res = 0;
        int[] cnt = str2cnt(chars);
        for (String word : words) {
            int[] wordCnt = str2cnt(word);
            boolean contain = true;
            for (int i = 0; i < cnt.length; i++) {
                if (wordCnt[i] > cnt[i]) {
                    contain = false;
                    break;
                }
            }
            if (contain) {
                res += word.length();
            }
        }
        return res;
    }
    private int[] str2cnt(String string) {
        int[] cnt = new int[26];
        for (char c : string.toCharArray()) {
            cnt[c - 'a'] += 1;
        }
        return cnt;
    }
}
