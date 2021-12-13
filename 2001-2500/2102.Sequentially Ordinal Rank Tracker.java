class SORTracker {
    private int counter;
    private PriorityQueue<Pair<String, Integer>> smaller;
    private PriorityQueue<Pair<String, Integer>> bigger;
    public SORTracker() {
        counter = 0;
        bigger = new PriorityQueue<Pair<String, Integer>>(
                       (a, b) -> b.getValue() - a.getValue() != 0 ? b.getValue() - a.getValue() : a.getKey().compareTo(b.getKey())
                    );
        smaller = new PriorityQueue<Pair<String, Integer>>(
                       (b, a) -> b.getValue() - a.getValue() != 0 ? b.getValue() - a.getValue() : a.getKey().compareTo(b.getKey())
                    );

    }
    
    public void add(String name, int score) {
        smaller.add(new Pair<String, Integer>(name, score));
        normalize();
    }
    
    public String get() {
        counter++;
        normalize();
        return smaller.peek().getKey();
    }
    private void normalize() {
        while (counter > smaller.size()) {
            smaller.add(bigger.poll());
        }
        while (counter < smaller.size()) {
            bigger.add(smaller.poll());
        }
    }
}

/**
 * Your SORTracker object will be instantiated and called as such:
 * SORTracker obj = new SORTracker();
 * obj.add(name,score);
 * String param_2 = obj.get();
 */

