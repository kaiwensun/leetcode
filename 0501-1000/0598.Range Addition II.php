class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer[][] $ops
     * @return Integer
     */
    function maxCount($m, $n, $ops) {
        foreach($ops as list($x, $y)) {
            $m = min($m, $x);
            $n = min($n, $y);
        }
        return $m * $n;
    }
}

