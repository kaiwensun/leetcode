import java.util.ArrayDeque

class Solution {
    fun clearDigits(s: String): String {
        var stack = ArrayDeque<Char>()
        for (c in s) {
            if (c.isDigit()) {
                stack.pop()
            } else {
                stack.push(c)
            }
        }
        return stack.joinToString("").reversed()
    }
}

