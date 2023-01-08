class Solution {

    /**
     * @param Integer[] $stations
     * @param Integer $r
     * @param Integer $k
     * @return Integer
     */
    function maxPower($stations, $r, $k) {
        $size = count($stations);
        $power = $this->calcPower($stations, $r, $size);
        print_r($power);
        $left = min($power);
        $right = $left + $k + 1;
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($this->test($power, $size, $mid, $r, $k)) {
                $left = $mid + 1;
            } else {
                $right = $mid;
            }
        }
        return $left - 1;
    }

    private function test($power, $size, $bar, $r, $k) {
        $drop = array();
        $cur = 0;
        for ($i = 0; $i < $size; $i++) {
            $diff = $bar - $power[$i] - $cur;
            if ($diff > 0) {
                $k -= $diff;
                if ($k < 0) {
                    return false;
                }
                $cur += $diff;
                $drop[$i + $r * 2] = $diff;
            }
            if ($drop[$i]) {
                $cur -= $drop[$i];
            }
        }
        return true;
    }

    private function calcPower($stations, $r, $size) {
        $power = array();
        $cur = 0;
        for ($i = 0; $i < min($r, $size); $i++) {
            $cur += $stations[$i];
        }
        for ($i = 0; $i < $size; $i++) {
            if ($i + $r < $size) {
                $cur += $stations[$i + $r];
            }
            $power[$i] = $cur;
            if ($i - $r >= 0) {
                $cur -= $stations[$i - $r];
            }
        }
        return $power;
    }
}

