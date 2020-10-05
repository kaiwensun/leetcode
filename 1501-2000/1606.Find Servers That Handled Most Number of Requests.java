class Solution {
    public List<Integer> busiestServers(int k, int[] arrival, int[] load) {
        PriorityQueue<int[]> busyServers = new PriorityQueue<>(new Comparator<int[]>() {
            // Min heap. Each element is {taskEndTime, serverId}
            @Override
            public int compare(int[] item1, int[] item2) {
                return item1[0] - item2[0];
            }
        });
        TreeSet<Integer> nextServerFinder = new TreeSet<>();
        for (int i = 0; i < k; i++) {
            nextServerFinder.add(i);
        }
        int[] counter = new int[k];
        for (int i = 0; i < arrival.length; i++) {
            while (!busyServers.isEmpty() && busyServers.peek()[0] <= arrival[i]) {
                int serverId = busyServers.poll()[1];
                nextServerFinder.add(serverId);
            }
            if (nextServerFinder.isEmpty()) {
                continue;
            }
            Integer nextServer = nextServerFinder.ceiling(i % k);
            if (nextServer == null) {
                nextServer = nextServerFinder.pollFirst();
            } else {
                nextServerFinder.remove(nextServer);
            }
            counter[nextServer] += 1;
            busyServers.add(new int[] {arrival[i] + load[i], nextServer});
        }
        int max = Arrays.stream(counter).max().getAsInt();
        return IntStream.range(0, k).filter(i -> counter[i] == max).boxed().collect(Collectors.toList());
    }
}

