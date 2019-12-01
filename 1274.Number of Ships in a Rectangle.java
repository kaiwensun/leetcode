/**
 * // This is Sea's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Sea {
 *     public boolean hasShips(int[] topRight, int[] bottomLeft);
 * }
 */

class Solution {
    public int countShips(Sea sea, int[] topRight, int[] bottomLeft) {
        if (topRight[0] < bottomLeft[0] || topRight[1] < bottomLeft[1] || !sea.hasShips(topRight, bottomLeft)) {
            return 0;
        }
        if (topRight[0] == bottomLeft[0] && topRight[1] == bottomLeft[1]) {
            return sea.hasShips(topRight, bottomLeft) ? 1 : 0;
        }
        if(topRight[0] == bottomLeft[0]) {
            int mid = (topRight[1] + bottomLeft[1]) / 2;
            int up = countShips(sea, topRight, new int[]{topRight[0], mid + 1});
            int low = countShips(sea, new int[]{bottomLeft[0], mid}, bottomLeft);
            return up + low;
        }
        int mid = (topRight[0] + bottomLeft[0]) / 2;
        int right = countShips(sea, topRight, new int[]{mid + 1, bottomLeft[1]});
        int left = countShips(sea, new int[]{mid, topRight[1]}, bottomLeft);
        return right + left;
    }
}
