class Bitset {
    private Set<Integer> set;
    private int size;
    private boolean flipped;

    public Bitset(int size) {
        set = new HashSet<>();
        this.size = size;
        flipped = false;
    }

    public void fix(int idx) {
        if (flipped) {
            set.remove(idx);
        } else {
            set.add(idx);
        }
    }

    public void unfix(int idx) {
        if (flipped) {
            set.add(idx);
        } else {
            set.remove(idx);
        }
    }

    public void flip() {
        flipped = !flipped;
    }

    public boolean all() {
        return set.size() == (flipped ? 0 : size);
    }

    public boolean one() {
        return flipped ? set.size() < size : !set.isEmpty();
    }

    public int count() {
        return flipped ? size - set.size() : set.size();
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < size; i++) {
            sb.append(set.contains(i) != flipped ? 1 : 0);
        }
        return sb.toString();
    }
}

/**
 * Your Bitset object will be instantiated and called as such:
 * Bitset obj = new Bitset(size);
 * obj.fix(idx);
 * obj.unfix(idx);
 * obj.flip();
 * boolean param_4 = obj.all();
 * boolean param_5 = obj.one();
 * int param_6 = obj.count();
 * String param_7 = obj.toString();
 */

