class Solution {
    public boolean isStrictlyPalindromic(int n) {
        /*
        When b = n - 2. n >= 4, so b >= 2.
        Suppose the palindromic digit is x. (x > 0)

          b + 2
        = n
        = x + x(b^1) + x(b^2) + ... + x(b^?)
        = x (1 + b^1 + b^2 + ... + b^?)
        >= (1 + b^1 + b^2 + ... + b^?)
        So, 1 >= b^2 + ... + b^?
        So either b == 0 or ? = 0
        But b >= 2.
        Also, ? cannot be 0, because ? = 0 means the palindromic number has only one digit. Obviously n expressed in (n-2) base must has more than one digit.
        Therefore, n is always not palindromic in n-2 base.
        */
        return false;
    }
}

