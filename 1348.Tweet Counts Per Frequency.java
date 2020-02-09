import java.util.TreeMap;
class TweetCounts {

    private TreeMap<Integer, Map<Integer, Integer>> bst;
    private Map<String, Integer> reg;

    private Integer compress(String tweetName) {
        Integer size = reg.size();
        Integer h = reg.putIfAbsent(tweetName, size);
        return h == null ? size : h;
    }
    public TweetCounts() {
        bst = new TreeMap<>();
        reg = new HashMap<>();
    }
    
    public void recordTweet(String tweetName, int time) {
        Integer code = compress(tweetName);
        Map<Integer, Integer> newCounter = new HashMap<>();
        newCounter.put(code, 1);
        Map<Integer, Integer> curCounter = bst.putIfAbsent(time, newCounter);
        if (curCounter != null) {
            curCounter.put(code, curCounter.getOrDefault(code, 0) + 1);
        }
    }
    
    private int getInterval(String freq) {
        switch (freq) {
            case "minute": return 60;
            case "hour": return 60 * 60;
            case "day": return 60 * 60 * 24;
            default: throw new RuntimeException();
        }
    }
    
    private List<Integer> genEmptyResult(int interval, int startTime, int endTime) {
        int size = (endTime - startTime) / interval + 1;
        List<Integer> res = new ArrayList<>(size);
        for (int i = 0; i < size; i++) res.add(0);
        return res;
    }
    public List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) {
        Integer code = compress(tweetName);
        int interval = getInterval(freq);
        List<Integer> res = genEmptyResult(interval, startTime, endTime);
        for (Map.Entry<Integer, Map<Integer, Integer>> entry: bst.subMap(startTime, endTime + 1).entrySet()) {
            int index = (entry.getKey() - startTime) / interval;
            int count = entry.getValue().getOrDefault(code, 0);
            res.set(index, res.get(index) + count);
        }
        return res;
    }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * TweetCounts obj = new TweetCounts();
 * obj.recordTweet(tweetName,time);
 * List<Integer> param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */
