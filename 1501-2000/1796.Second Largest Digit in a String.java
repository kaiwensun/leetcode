class Solution {
    public int secondHighest(String s) {
        int fst = -1, snd = -1;
        for (char c : s.toCharArray()) {
            if (c <= '9') {
                int num = c - '0';
                if (num > fst) {
                    int tmp = fst; fst = num; num = tmp;
                }
                if (num < fst && num > snd) {
                    int tmp = snd; snd = num; num = tmp;
                }
            }
        }
        return snd;

    }
}

