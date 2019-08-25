class Solution {
    public String lastSubstring(String s) {
        int bossHead = 0;
        int currHead = 0;
        int i = 0;
        for (i = 0; i < s.length(); i++) {
            if (bossHead == currHead) {
                currHead ++;
                continue;
            }
            int length = i - currHead;
            char bossChar = s.charAt(bossHead + length);
            char currChar = s.charAt(currHead + length);
            if (bossChar < currChar) {
                bossHead = currHead;
                if (s.charAt(bossHead) < currChar) {
                    bossHead = i;
                    currHead = i + 1;
                } else if (s.charAt(bossHead) == currChar) {
                    currHead = i;
                    if (currHead == bossHead) {
                        currHead ++;
                    }
                }
            } else if (bossChar > currChar) {
                currHead = i + 1;
            }
        }
        return s.substring(bossHead);
    }
}
