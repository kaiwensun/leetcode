class Solution {
    public boolean canReach(int[] arr, int index) {
        if (0 <= index && index < arr.length && arr[index] != -1) {
            int val = arr[index];
            arr[index] = -1;
            return val == 0 || canReach(arr, index + val) || canReach(arr, index - val);
        }
        return false;
    }
}
