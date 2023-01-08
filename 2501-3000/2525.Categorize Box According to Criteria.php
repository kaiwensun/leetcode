class Solution {

    /**
     * @param Integer $length
     * @param Integer $width
     * @param Integer $height
     * @param Integer $mass
     * @return String
     */
    function categorizeBox($length, $width, $height, $mass) {
        $bulky = max($length, $width, $height) >= 10 ** 4 || $length * $width * $height >= 10 ** 9;
        $heavy = $mass >= 100;
        if ($heavy && $bulky) return "Both";
        if (!$heavy && !$bulky) return "Neither";
        return $heavy ? "Heavy" : "Bulky";
    }
}

