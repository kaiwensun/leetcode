class Solution {
    private int[] chargeTimes;
    private int[] runningCosts;
    private long sumRunningCosts = 0;
    private int k = 0;
    private TreeMap<Integer, Integer> chargeTimesInWindow = new TreeMap<>();

    private void init(int[] chargeTimes, int[] runningCosts) {
        this.chargeTimes = chargeTimes;
        this.runningCosts = runningCosts;
    }

    public int maximumRobots(int[] chargeTimes, int[] runningCosts, long budget) {
        init(chargeTimes, runningCosts);
        int left = 0;
        int res = 0;
        for (int right = 0; right < chargeTimes.length; right++) {
            add(right);
            while (getCost() > budget) {
                remove(left++);
            }
            res = Math.max(res, k);
        }
        return res;
    }

    private void add(int i) {
        this.sumRunningCosts += runningCosts[i];
        k++;
        chargeTimesInWindow.put(chargeTimes[i], chargeTimesInWindow.getOrDefault(chargeTimes[i], 0) + 1);
    }

    private void remove(int i) {
        this.sumRunningCosts -= runningCosts[i];
        k--;
        chargeTimesInWindow.put(chargeTimes[i], chargeTimesInWindow.get(chargeTimes[i]) - 1);
        if (chargeTimesInWindow.get(chargeTimes[i]) == 0) {
            chargeTimesInWindow.remove(chargeTimes[i]);
        }
    }

    private long getCost() {
        return k == 0 ? 0 : chargeTimesInWindow.lastKey() + k * sumRunningCosts;
    }
}

