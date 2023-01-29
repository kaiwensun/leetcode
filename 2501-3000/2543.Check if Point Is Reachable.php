class Solution {

    /**
     * @param Integer $targetX
     * @param Integer $targetY
     * @return Boolean
     */
    function isReachable($targetX, $targetY) {
        if ($targetX > $targetY) {
            $tmp = $targetY; $targetY = $targetX; $targetX = $tmp;
        }
        while ($targetX) {
            $targetY %= $targetX;
            $tmp = $targetY; $targetY = $targetX; $targetX = $tmp;
        }
        return ($targetY & ($targetY - 1)) == 0;
    }
}

