class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function differenceOfSum($nums) {
        $ele = $dig = 0;
        foreach ($nums as $num) {
            $ele += $num;
            while ($num) {
                $dig += $num % 10;
                $num = intdiv($num, 10);
            }
        }
        return abs($ele - $dig);
    }
}

