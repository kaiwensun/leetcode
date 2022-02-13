class Solution {
    public int countOperations(int num1, int num2) {
        int res = 0;
        if (num2 > num1) {
            int tmp = num1; num1 = num2; num2 = tmp;
        }
        while (num2 != 0) {
            res += num1 / num2;
            int tmp = num1 % num2; num1 = num2; num2 = tmp;
        }
        return res;
    }
}

