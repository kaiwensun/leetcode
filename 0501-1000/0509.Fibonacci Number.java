class Solution {
    private int[] cache = new int[31];
    public int fib(int n) {
        if (n <= 1) {
            return n;
        }
        if (cache[n] != 0) {
            return cache[n];
        }
        cache[n] = fib(n -1) + fib(n - 2);
        return cache[n];
    }
}

