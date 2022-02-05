class Solution {
    public long minimumDifference(int[] nums) {
        final int N = nums.length / 3;

        ArrayList<Long> minLeftSumDP = new ArrayList(N);

        Queue<Integer> leftNums = new PriorityQueue<>(N, (a, b) -> b - a);
        long leftSum = 0;
        for (int i = 0; i < N; i++) {
            leftSum += nums[i];
            leftNums.add(nums[i]);
        }
        long minLeftSum = leftSum;
        for (int i = 0; i < N; i++) {
            minLeftSumDP.add(minLeftSum);
            int num = nums[i + N];
            leftSum += num;
            leftNums.add(num);
            leftSum -= leftNums.poll();
            minLeftSum = Math.min(minLeftSum, leftSum);
        }

        Queue<Integer> rightNums = new PriorityQueue<>(N);
        long rightSum = 0;
        for (int i = N * 2; i < N * 3; i++) {
            rightSum += nums[i];
            rightNums.add(nums[i]);
        }

        long res = minLeftSum - rightSum;
        long maxRightSum = rightSum;
        for (int i = N * 2 - 1; i >= N; i--) {
            int num = nums[i];
            rightSum += num;
            rightNums.add(num);
            rightSum -= rightNums.poll();
            maxRightSum = Math.max(maxRightSum, rightSum);
            res = Math.min(res, minLeftSumDP.get(i - N) - maxRightSum);
        }

        return res;
    }
}

