class Solution {
    public String maximumBinaryString(String binary) {
        char[] chars = binary.toCharArray();
        int l = 0;
        while (l < chars.length && chars[l] != '0') l++;
        int r = l + 1;
        while (r < chars.length && chars[r] != '0') r++;
        while (r < chars.length) {
            if (chars[r] == '0') {
                chars[r] = '1';
                chars[l++] = '1';
                chars[l] = '0';
            }
            r++;
        }
        return new String(chars);
    }
}

