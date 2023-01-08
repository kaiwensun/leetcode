class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function xorBeauty($nums) {
        $size = count($nums);
        $res = 0;
        for ($mask = 1; $mask < 1 << 31; $mask <<= 1) {
            $res |= $this->getBit($mask, $nums, $size);
        }
        return $res;
    }
    private function getBit($mask, $nums, $size) {
        $ones = count(array_filter($nums, function($num) use($mask) { return $num & $mask; }));
        $zeros = $size - $ones;
        return (($size * $size - $zeros * $zeros) * $ones & 1) ? $mask : 0;
    }
}

