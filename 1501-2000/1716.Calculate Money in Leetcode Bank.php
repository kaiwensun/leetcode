class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function totalMoney($n) {
        $week = floor($n / 7);
        $day = $n % 7;
        return 28 * $week + ($week - 1) * $week / 2 * 7 + ($week + $week + $day + 1) * $day / 2;
    }
}

