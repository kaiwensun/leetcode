/**
 *Basic idea:
 * Use Double-ended Queue. Store the index of numbers and abandon those out of range and those can never be max. see comments.
 *Result:
 * 18 / 18 test cases passed.
 * Status: Accepted
 * Runtime: 22 ms
 * Your runtime beats 66.23% of java submissions.
 *Date:
 * 9/21/2016
 */
public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if(k==0)
            return new int[0];
        Deque<Integer> indices = new ArrayDeque<Integer>();
        int[] res = new int[nums.length-k+1];
        for(int i=0;i<nums.length;i++){
            //remove those out of the range k
            while(!indices.isEmpty() && indices.peek()<=i-k)
                indices.poll();
            //remove those reached before i and less than nums[i], because they will never be the max in the future.
            while(!indices.isEmpty() && nums[indices.peekLast()]<=nums[i])
                indices.pollLast();
            //add i to deque
            indices.offer(i);
            //the deque is a strictly decreasing queue. So its head corresponds to the max.
            if(i-k+1>=0)
                res[i-k+1] = nums[indices.peek()];
        }
        return res;
    }
}
