class Solution {
    public int minGroups(int[][] intervals) {
        Queue<Integer> endings = new PriorityQueue<>();
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        for (int[] interval : intervals) {
            if (endings.peek() != null && endings.peek() < interval[0]) {
                endings.remove();
            }
            endings.offer(interval[1]);
        }
        return endings.size();
    }
}

