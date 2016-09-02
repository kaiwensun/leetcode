/**
 *Basic idea:
 * View Each bit independently. Count the appearance by pushing the flag bit (1) circularly from `one` to `three`. Detailed explination is at the end of the code.
 *Result:
 * 11 / 11 test cases passed.
 * Status: Accepted
 * Runtime: 1 ms
 * Your runtime beats 86.59% of javasubmissions.
 *Date:
 * 9/2/2016
 */
public class Solution {
    public int singleNumber(int[] nums) {
        int one = -1;
        int two = 0;
        int three = 0;
        for(int e : nums){
            int tmpthree = three;
            three = (three&~e) | (two & e);
            two = (two&~e) | (one & e);
            one = (one&~e) | (tmpthree & e);
        }
        return two;
    }
}

/*
Detailed explination:
This solution is inspired by and based on @againest1 's solution at [here](https://discuss.leetcode.com/topic/2031/challenge-me-thx) and @woshidaishu 's explanation in the [follow-up](https://discuss.leetcode.com/topic/2031/challenge-me-thx/17). Thank you, guys!

In againest1's solution, many people are wondering how did he come up with the true table. Well, here in my solution, the state transition is pretty straightforward.

```
public class Solution {
    public int singleNumber(int[] nums) {
        int one = -1;
        int two = 0;
        int three = 0;
        for(int e : nums){
            int tmpthree = three;
            three = (three&~e) | (two & e);
            two = (two&~e) | (one & e);
            one = (one&~e) | (tmpthree & e);
        }
        return ~one;
    }
}
```
The basic idea is that we view each bit individually and independently. We count the appearance of each bit by pushing the flag bit (1, initiated by `int one=-1`) circularly from `one` to `two`, then to `three`, and then to `one`, and repeat it. Every bit 1 is "following forward" by one step when the corresponding bit in `e` is 1.

Take the line `three = (three&~e) | (two & e);` for example. 
* `e` serves as a mask.
* `(two &e)` is extracting the bits in `two` masked by `e`. It is the bits that we want to push to `three`.
* `(three&~e)` is extracting the bits not masked by `e`. It is the bits that we want to keep remained in `three`.
* `three = (three&~e) | (two & e)` is the result of new `three` after pushing the masked bits of `two` forward to `three`.

Finally, after traversing all numbers, `two` is the single number. `~one==two`.

This solution is still correct in cases like `[1,1,1,2,2,2,3,3]` and `[1,1,1,1,1,1,2]`.
With small changes, this solution is also adaptive to questions like:
* "Every element appears k (k>1) times except for one." (Replace variables `one`, `two`, `three` with an array of length k. Time complexity is O(nk). )
* "Every element appears k (k>2) times except for one appearing k-1 times and one appearing k-2 times. (return non-zero values of `two`, `three`, `four`, etc.)
*/
