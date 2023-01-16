class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @param String $baseStr
     * @return String
     */
    function smallestEquivalentString($s1, $s2, $baseStr) {
        $data = array();

        foreach (str_split("qwertyuiopasdfghjklzxcvbnm") as $c) {
            $data[$c] = $c;
        }
        for ($i = 0; $i < strlen($s1); $i++) {
            $this->union($s1[$i], $s2[$i], $data);
        }
        $res = "";
        foreach (str_split($baseStr) as $c) {
            $res .= $this->find($c, $data);
        }
        return $res;
    }

    private function find($c, &$data) {
            if ($data[$c] != $c) {
                $data[$c] = $this->find($data[$c], $data);
            }
            return $data[$c];
        }

    private function union($x, $y, &$data) {
        $rx = $this->find($x, $data);
        $ry = $this->find($y, $data);
        if ($rx < $ry) {
            $data[$ry] = $rx;
        } else {
            $data[$rx] = $ry;
        }
    }
}

