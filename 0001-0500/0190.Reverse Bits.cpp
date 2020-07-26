/**
 *Result:
 * 600 / 600 test cases passed.
 * Status: Accepted
 * Runtime: 3 ms
 * Your runtime beats 34.43% of cpp submissions.
 *Date:
 * 11/15/2016
 */
class Solution {
private:
    uint32_t map[0x10] ={0x0,0x8,0x4,0xC,0x2,0xA,0x6,0xE,0x1,0x9,0x5,0xD,0x3,0xB,0x7,0xF};
public:
    uint32_t reverseBits(uint32_t n) {
        return map[n>>28] | (map[(n>>24)&0xF]<<4) | (map[(n>>20)&0xF]<<8) | (map[(n>>16)&0xF]<<12)
        | (map[(n>>12)&0xF]<<16) | (map[(n>>8)&0xF]<<20) | (map[(n>>4)&0xF]<<24) | (map[n&0xF]<<28);
    }
};
