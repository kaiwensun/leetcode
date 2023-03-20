class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximizeGreatness($nums) {
        sort($nums);
        $slow = 0;
        for ($fast = 0; $fast < count($nums); $fast++) {
            while ($fast < count($nums) && $nums[$fast] <= $nums[$slow]) {
                $fast++;
            }
            if ($fast < count($nums)) {
                $slow++;
            }
        }
        return $slow;
    }
}

