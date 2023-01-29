import java.util.PriorityQueue;
import java.util.stream.IntStream;

class Solution {
    private long sum = 0;
    private PriorityQueue<Integer> heap;
    public long maxScore(int[] nums1, int[] nums2, int k) {
        long sum = 0;
        long res = 0;
        PriorityQueue<Integer> heap = new PriorityQueue<>(k, (i, j) -> nums1[i] - nums1[j]);;
        for (int i : IntStream.range(0, nums1.length).boxed().sorted((i, j) -> nums2[j] - nums2[i]).mapToInt(x -> x).toArray()) {
            if (heap.size() == k) {
                sum -= nums1[heap.poll()];
            }
            sum += nums1[i];
            heap.add(i);
            if (heap.size() == k) {
                res = Math.max(res, sum * nums2[i]);
            }
        };
        return res;
    }
}
