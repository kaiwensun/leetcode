/**
 *Basic idea:
 * LinkedHashMap, a data structure extending HashMap but also preserveing orders of entries.
 *Result:
 * 17 / 17 test cases passed.
 * Status: Accepted
 * Runtime: 15 ms
 * Your runtime beats 92.56% of java submissions.
 *Date:
 * 10/27/2016
 */
class LRUCache {
    private Map<Integer,Integer>map; 
    public LRUCache(int capacity) {
        map = new LinkedHashMap<Integer,Integer>(capacity, 0.75f, true){
        	@Override
        	protected boolean removeEldestEntry(Map.Entry<Integer,Integer> eldest){
        		return size()>capacity;
        	}
        };
    }
    
    public int get(int key) {
        return map.getOrDefault(key, -1);
    }
    
    public void set(int key, int value) {
        map.put(key,value);
    }
}
