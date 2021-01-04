class Solution {
    public List<List<Integer>> largeGroupPositions(String s) {
        char letter = ' ';
        int start = 0;
        List<List<Integer>> res = new ArrayList<>();
        for (int end = 0; end <= s.length(); end++) {
            char cur = end == s.length() ? ' ' : s.charAt(end);
            if (cur != letter) {
                letter = cur;
                if (end - start >= 3) {
                    res.add(Arrays.asList(start, end - 1));
                }
                start = end;
            }
        }
        return res;
    }
}

