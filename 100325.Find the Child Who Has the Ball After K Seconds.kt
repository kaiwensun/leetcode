class Solution {
    fun numberOfChild(n: Int, k: Int): Int {
        val res = k % ((n - 1) * 2)
        return if (res < n - 1) res else (n - 1) * 2 - res
    }
}

