class Solution {
    public String largestTimeFromDigits(int[] A) {
        Arrays.sort(A);
        int hr10 = 2;
        for (int hr10UpperBound : new int[] {2, 1}) {
            if (hr10 != 2) break;
            int[] B = A.clone();
            hr10 = takeBiggestUnder(hr10UpperBound, B);
            if (hr10 == -1) continue;
            int hr1UpperBound = hr10 == 2 ? 3 : 9;
            int hr1 = takeBiggestUnder(hr1UpperBound, B);
            if (hr1 == -1) continue;
            int mn10 = takeBiggestUnder(5, B);
            if (mn10 == -1) continue;
            int mn1 = takeBiggestUnder(9, B);
            return String.format("%d%d:%d%d", hr10, hr1, mn10, mn1);
        }
        return "";
    }
    
    private int takeBiggestUnder(int upperBound, int[] A) {
        int resInd = -1;
        int[] AClone = A.clone();
        for (int i = A.length - 1; i >= 0; i--) {
            if (A[i] <= upperBound && A[i] != -1) {
                int res = A[i];
                A[i] = -1;
                return res;
            }
        }
        return -1;
    }
}

