import java.util.Arrays;

class Solution {
    public int lengthOfLIS(int[] nums, int k) {
        int[] segTree = new int[(Arrays.stream(nums).max().getAsInt() + 1) * 2];
        Arrays.fill(segTree, 0);
        for (int i = 0; i < nums.length; i++) {
            int left = Math.max(0, nums[i] - k);
            int right = nums[i];
            int maxValue = maximum(left, right, segTree) + 1;
            set(nums[i], maxValue, segTree);
        }
        return segTree[1];
    }

    private int maximum(int left, int right, int[] segTree) {
        int n = segTree.length / 2;
        left += n;
        right += n;
        int res = 0;
        while (left < right) {
            if (left % 2 == 1) {
                res = Math.max(res, segTree[left++]);
            }
            if (right % 2 == 1) {
                res = Math.max(res, segTree[--right]);
            }
            left >>= 1;
            right >>= 1;
        }
        return res;
    }

    private void set(int index, int value, int[] segTree) {
        int n = segTree.length / 2;
        index += n;
        segTree[index] = Math.max(segTree[index], value);
        while (index != 0) {
            segTree[index >> 1] = Math.max(segTree[index >> 1], segTree[index]);
            index >>= 1;
        }
    }
}

