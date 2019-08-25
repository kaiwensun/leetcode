class FileSystem {
    private final Map<String, Integer> map;

    public FileSystem() {
        map = new HashMap<>();
    }
    
    public boolean create(String path, int value) {
        int lastIndex = path.lastIndexOf('/');
        if (lastIndex == 0) {
            if (get(path) != -1) {
                return false;
            }
        } else {
            String parent = path.substring(0, lastIndex);
            if (get(parent) == -1 || get(path) != -1) {
                return false;
            }
        }
        map.put(path, value);
        return true;
    }
    
    public int get(String path) {
        return map.getOrDefault(path, -1);
    }
}

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem obj = new FileSystem();
 * boolean param_1 = obj.create(path,value);
 * int param_2 = obj.get(path);
 */
