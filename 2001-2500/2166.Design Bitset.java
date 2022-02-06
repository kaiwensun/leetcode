class Bitset {

    private final static int INT_SIZE = 31;
    private int size;
    private List<Integer> buffer;
    private int count;
    private boolean flipped;

    public Bitset(int size) {
        this.size = size;
        this.count = 0;
        this.flipped = false;
        int buckets = (size + INT_SIZE - 1) / INT_SIZE;
        this.buffer = new ArrayList(buckets);
        for (int i = 0; i < buckets; i++) {
            this.buffer.add(0);
        }
    }

    private int get(int idx) {
        if ((this.buffer.get(idx / INT_SIZE) & (1 << (INT_SIZE - 1 - idx % INT_SIZE))) == 0) {
            return flipped ? 1 : 0;
        } else {
            return flipped ? 0 : 1;
        }
    }

    private void set(int idx, int value) {
        int cell = this.buffer.get(idx / INT_SIZE);
        int mask = 1 << (INT_SIZE - 1 - idx % INT_SIZE);
        if ((value == 0) != flipped) {
            cell &= ~mask;
        } else {
            cell |= mask;
        }
        this.buffer.set(idx / INT_SIZE, cell);
    }

    public void fix(int idx) {
        int val = get(idx);
        if (val == 0) {
            this.count++;
            set(idx, 1);
        }
    }

    public void unfix(int idx) {
        int val = get(idx);
        if (val == 1) {
            this.count--;
            set(idx, 0);
        }
    }

    public void flip() {
        flipped = !flipped;
        count = size - count;
    }

    public boolean all() {
        return size == count;
    }

    public boolean one() {
        return count > 0;
    }

    public int count() {
        return count;
    }

    public String toString() {
        StringBuffer sb = new StringBuffer();
        for (Integer num : buffer) {
            sb.append(Integer.toBinaryString(0x80000000 | (flipped ? ~num : num)).substring(1));
        }
        return sb.substring(0, size).toString();
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

