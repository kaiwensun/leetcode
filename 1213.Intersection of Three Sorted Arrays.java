class Solution {
    public List<Integer> arraysIntersection(int[] arr1, int[] arr2, int[] arr3) {
        int indexes[] = new int[]{0, 0, 0};
        int[][] arrs = new int[][]{arr1, arr2, arr3};
        List<Integer> res = new ArrayList<>();
        while (IntStream.range(0, 3).allMatch(i -> indexes[i] < arrs[i].length)) {
            Integer min = IntStream.range(0, 3).map(i -> arrs[i][indexes[i]]).min().getAsInt();
            if (IntStream.range(0, 3).allMatch(i -> min == arrs[i][indexes[i]])) {
                res.add(arrs[0][indexes[0]]);
            }
            IntStream.range(0, 3).filter(i -> min == arrs[i][indexes[i]]).forEach(i -> indexes[i] += 1);
        }
        return res;
    }
}
