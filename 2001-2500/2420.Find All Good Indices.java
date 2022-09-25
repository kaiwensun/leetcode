class Solution {
    public List<Integer> goodIndices(int[] nums, int k) {
        final int N = nums.length;
        int[] tailSize = new int[N];
        int size = 1;
        for (int i = N - 2; i >= k - 1; i--) {
            tailSize[i] = size;
            if (nums[i] > nums[i + 1]) {
                size = 1;
            } else {
                size++;
            }
        }
        size = 1;
        List<Integer> res = new LinkedList<>();
        for (int i = 1; i < N - k; i++) {
            if (size >= k && tailSize[i] >= k) {
                res.add(i);
            }
            if (nums[i] > nums[i - 1]) {
                size = 1;
            } else {
                size++;
            }
        }
        return res;
    }
}

