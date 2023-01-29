class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function alternateDigitSum($n) {
        $s = strval($n);
        $res = 0;
        for ($i = 0; $i < strlen($s); $i++) {
            $res += ($i % 2 == 0 ? 1 : -1) * intval($s[$i]);
        }
        return $res;
    }
}

