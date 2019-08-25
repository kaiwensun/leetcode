class Solution {
    public int calculateTime(String keyboard, String word) {
        Map<Integer, Integer> map = new HashMap<>();
        keyboard.chars().reduce(0, (index, c) -> {map.put(c, index); return index + 1;});
        int lastChar = map.get((int)(word.charAt(0)));
        List<Integer> lastCharWrapper = Arrays.asList(new Integer[]{lastChar});
        return word.chars().reduce(
            0,
            (acc, c) -> {
                acc += Math.abs(map.get(lastChar) - map.get(c));
                lastCharWrapper.set(0, c);
                return acc;
            }
        );
    }
}
