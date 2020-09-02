class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        boolean swapped = false;
        if (nums1.length > nums2.length) {
            int[] tmp = nums1;
            nums1 = nums2;
            nums2 = tmp;
            swapped = true;
        }
        final int[] arr1 = nums1;
        final int[] arr2 = nums2;
        int size1 = k < arr1.length ? k : arr1.length;
        int size2 = k < arr2.length ? k : arr2.length;
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>(size1 + 1, new Comparator<int[]>() {
            @Override
            public int compare(int[] indPair1, int[] indPair2) {
                return (arr1[indPair1[0]] + arr2[indPair1[1]]) - (arr1[indPair2[0]] + arr2[indPair2[1]]);
            }
        });
        for (int i = 0; i < size1; ++i) {
            pq.add(new int[]{i, 0});
        }
        List<List<Integer>> result = new LinkedList<>();
        for (int i = 0; i < k && !pq.isEmpty(); ++i) {
            int[] indPair = pq.poll();
            if (swapped) {
                result.add(Arrays.asList(arr2[indPair[1]], arr1[indPair[0]]));
            } else {
                result.add(Arrays.asList(arr1[indPair[0]], arr2[indPair[1]]));
            }
            if (++indPair[1] < size2) {
                pq.add(indPair);
            }
        }
        return result;
    }
}
