class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function countGood($nums, $k) {
        $cnt = array();
        $l = $paris = $res = 0;
        foreach ($nums as $num) {
            $pairs += $cnt[$num];
            $cnt[$num]++;
            while ($pairs - ($cnt[$nums[$l]] - 1) >= $k) {
                $pairs -= $cnt[$nums[$l]] - 1;
                $cnt[$nums[$l]]--;
                $l++;
            }
            if ($pairs >= $k) {
                $res += $l + 1;
            }
        }
        return $res;
    }
}


