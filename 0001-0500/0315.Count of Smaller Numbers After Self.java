class Solution {
    public List<Integer> countSmaller(int[] nums) {
        int N = normalize(nums);
        int[] segTree = new int[N * 2];
        List<Integer> res = new ArrayList<>(nums.length);
        for (int i = nums.length - 1; i >= 0; i--) {
            res.add(query(0, nums[i], segTree, N));
            incSegTree(nums[i], segTree, N);
        }
        Collections.reverse(res);
        return res;
    }

    private int query(int start, int end, int[] segTree, final int N) {
        int res = 0;
        start += N;
        end += N;
        while (start < end) {
            if ((start & 1) == 1) {
                res += segTree[start];
                start += 1;
            }
            if ((end & 1) == 1) {
                end -= 1;
                res += segTree[end];
            }
            start >>= 1;
            end >>= 1;
        }
        return res;
    }

    private void incSegTree(int index, int[] segTree, final int N) {
        index += N;
        while (index != 0) {
            segTree[index] += 1;
            index >>= 1;
        }
    }

    private int normalize(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        List<Integer> array = new ArrayList<>(set);
        Collections.sort(array);
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < array.size(); i++) {
            map.put(array.get(i), i);
        }
        for (int i = 0; i < nums.length; i++) {
            nums[i] = map.get(nums[i]);
        }
        return map.size();
    }
}

