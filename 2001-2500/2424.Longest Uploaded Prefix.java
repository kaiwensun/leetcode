class LUPrefix {

    private boolean[] uploaded;
    private int i;
    public LUPrefix(int n) {
        i = 0;
        uploaded = new boolean[n + 1];
    }

    public void upload(int video) {
        uploaded[video - 1] = true;
    }

    public int longest() {
        while (uploaded[i]) {
            i++;
        }
        return i;
    }
}

