/**
 *Result:
 * 31 / 31 test cases passed.
 * Status: Accepted
 * Runtime: 7 ms
 * We are in the progress of updating the graph distribution. Please check the distribution again within weeks.
 *Date:
 * 9/18/2016
 */
public class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>(k);
        for(int i=0;i<k;i++){
            heap.offer(nums[i]);
        }
        for(int i=k;i<nums.length;i++){
            if(heap.peek()<nums[i]){
                heap.poll();
                heap.offer(nums[i]);
            }
        }
        return heap.peek();
    }
}
