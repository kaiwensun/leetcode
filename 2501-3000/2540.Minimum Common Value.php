class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function getCommon($nums1, $nums2) {
        $sz1 = count($nums1);
        $sz2 = count($nums2);
        $p1 = $p2 = 0;
        while ($p1 < $sz1 && $p2 < $sz2) {
            $n1 = $nums1[$p1];
            $n2 = $nums2[$p2];
            if ($n1 == $n2) return $n1;
            else if ($n1 < $n2) $p1++;
            else $p2++;
        }
        return -1;
    }
}

