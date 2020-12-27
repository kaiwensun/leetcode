class Solution {
    public double averageWaitingTime(int[][] customers) {
        long total = 0;
        long now = 0;
        for (int[] customer : customers) {
            if (now < customer[0]) {
                now = customer[0];
            }
            now += customer[1];
            total += now - customer[0];
        }
        return (double)total / customers.length;
    }
}

