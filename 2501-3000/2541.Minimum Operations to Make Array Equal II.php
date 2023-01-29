class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer
     */
    function minOperations($nums1, $nums2, $k) {
        $acc_diff = $res = 0;
        $size = count($nums1);
        for ($i = 0; $i < $size; $i++) {
            $diff = $nums1[$i] - $nums2[$i];
            if ($k == 0) {
                if($diff == 0) continue;
                else return -1;
            }
            if ($diff % $k == 0) {
                $acc_diff += $diff;
                $res += abs($diff);
            } else {
                return -1;
            }
        }
        if ($k == 0) return 0;
        return $acc_diff == 0 ? $res / $k / 2 : -1;
    }
}

