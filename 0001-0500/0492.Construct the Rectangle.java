class Solution {
    public int[] constructRectangle(int area) {
        int w = (int)Math.sqrt(area) + 1;
        while (true) {
            if (area % --w == 0) {
                return new int[] {area / w, w};
            }
        }
    }
}

