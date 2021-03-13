class MyHashMap {

     private final static int SIZE = 1 << 13;
     private final static Random random = new Random();
     private int mask;
     private List<List<int[]>> buckets;


    /** Initialize your data structure here. */
    public MyHashMap() {
        mask = random.nextInt(SIZE);
        buckets = new ArrayList<>(SIZE);
        for (int i = 0; i < SIZE; i++) {
            buckets.add(new ArrayList<>());
        }
    }
    
    /** value will always be non-negative. */
    public void put(int key, int value) {
        List<int[]> bucket = getBucket(key);
        for (int[] pair : bucket) {
            if (pair[0] == key) {
                pair[1] = value;
                return;
            }
        }
        bucket.add(new int[] {key, value});
    }

    private List<int[]> getBucket(int key) {
        int bucket_id = (key ^ mask) % SIZE;
        return buckets.get(bucket_id);
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    public int get(int key) {
        for (int[] pair: getBucket(key)) {
            if (pair[0] == key) {
                return pair[1];
            }
        }
        return -1;
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    public void remove(int key) {
        List<int[]> bucket = getBucket(key);
        for (int i = 0; i < bucket.size(); i++) {
            if (bucket.get(i)[0] == key) {
                bucket.set(i, bucket.get(bucket.size() - 1));
                bucket.remove(bucket.size() - 1);
                break;
            }
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */

