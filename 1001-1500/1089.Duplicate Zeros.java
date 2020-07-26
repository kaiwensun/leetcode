class Solution {
    public void duplicateZeros(int[] arr) {
        int i = 0, j = 0;
        for (; j < arr.length; j += arr[i] == 0 ? 2 : 1, i++) {}
        for (i--, j--; i > 0 && j > 0 ;i--, j--) {
            if (j < arr.length) {
                arr[j] = arr[i];
            }
            if (arr[i] == 0 && j >= 0) {
                arr[--j] = 0;
            }
        }
    }
}
