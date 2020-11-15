/**
 First (incorrect) thought: 
 When there are p pigs, group buckets into (p+1) groups. let each pig drink bucket water of its group.
 This algorithm requires more pigs than necessary. So in sound round, there must be some bucket drunk by more than one pigs.
 How to arrange multiple pigs to drink certain shared buckets in an manageable way? We need to encode buckets!

 Encoding buckets:
 How to encode buckets? Use k-base integer! Each pig is in charge of its own k-base bit. In round i (0-indexed), each pig checks the bit that it owns. If the number of that bit equals to i, the pig drinks it. If the pig dies, then we know the posionous bucket has value i at this bit.
 Pigs can drink r rounds, from 0 to r - 1. If after the r rounds the pig is still alive, we know the posionous bucket has value r at this bit.
 So we need the minimum number of bits to encode all buckets. The number of bits is the number of pigs.

 Why is this the optimal solution?
 We detect posionous bucket by observing pigs' status. There are `buckets` number of states. With the limited round of drinks, we need to make sure pigs' status space is big enough to represent all possible states of buckets. With fewer pigs, the pig space will not be big enough to distinguish certain bucket states.
 */
class Solution {
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        final int round = minutesToTest / minutesToDie;
        if (buckets != 0) {
            buckets -= 1;
        }
        int res = 0;
        while (buckets != 0) {
            buckets /= round + 1;
            res ++;
        }
        return res;
    }
}

