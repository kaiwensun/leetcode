class Solution {
    public int calculateTime(String keyboard, String word) {
        Map<Integer, Integer> map = new HashMap<>();
        keyboard.chars().reduce(0, (index, c) -> {map.put(c, index); return index + 1;});
        List<Integer> lastCharWrapper = Arrays.asList(new Integer[]{0});
        return word.chars().reduce(
            0,
            (acc, c) -> {
                acc += Math.abs(lastCharWrapper.get(0) - map.get(c));
                lastCharWrapper.set(0, map.get(c));
                return acc;
            }
        );
    }
}
