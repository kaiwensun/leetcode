class DataStream {

    private $value;
    private $k;
    private $cnt;

    /**
     * @param Integer $value
     * @param Integer $k
     */
    function __construct($value, $k) {
        $this->value = $value;
        $this->k = $k;
        $this->cnt = 0;

    }

    /**
     * @param Integer $num
     * @return Boolean
     */
    function consec($num) {
        $this->cnt = ($num == $this->value) ? $this->cnt + 1 : 0;
        return $this->cnt >= $this->k;
    }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * $obj = DataStream($value, $k);
 * $ret_1 = $obj->consec($num);
 */

