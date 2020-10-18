class Solution {
    final static String DNA = "ACGT";
    public List<String> findRepeatedDnaSequences(String s) {
        List<String> res = new ArrayList<>();
        final int MASK = (1 << 20) - 1;
        int roll = 0;
        
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            roll <<= 2;
            roll &= MASK;
            roll |= DNA.indexOf(s.charAt(i));
            if (i >= 9) {
                if (Integer.valueOf(1).equals(seen.put(roll, seen.getOrDefault(roll, 0) + 1))) {
                    res.add(s.substring(i - 9, i + 1));
                }
            }
        }
        return res;
    }
}

