class Solution {
    public int[] fraction(int[] cont) {
        int numerator = cont[cont.length - 1];
        int denominator = 1;
        for (int i = cont.length - 2; i >= 0; i--) {
            int tmp = numerator; numerator = denominator; denominator = tmp;
            numerator = cont[i] * denominator + numerator;
        }
        int gcd = getGcd(numerator, denominator);
        return new int[] {numerator / gcd, denominator / gcd};
    }

    private int getGcd(int a, int b) {
        if (a < b) {
            int tmp = a; a = b; b = tmp;
        }
        while (a % b != 0) {
            int tmp = a;
            a = b;
            b = tmp % b;
        }
        return b;
    }
}

