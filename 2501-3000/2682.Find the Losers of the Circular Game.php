class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer[]
     */
    function circularGameLosers($n, $k) {
        $i = 0;
        $diff = 0;
        $seen = array();
        while (!$seen[$i]) {
            $seen[$i] = true;
            $diff += $k;
            $k %= $n;
            $i += $diff;
            $i %= $n;
        }
        $res = array();
        for ($i = 0; $i < $n; $i++) {
            if (!$seen[$i]) {
                array_push($res, $i + 1);
            }
        }
        return $res;
    }
}

