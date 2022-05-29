/**
 * @param {number[]} nums
 * @return {number}
 */
var totalSteps = function(nums) {
    let toDelete = [];
    let cur ={};
    let res = 0;
    for (let i = 0; i < nums.length; i++) {
        if (cur.value > nums[i]) {
            toDelete.push(cur);
        }
        cur.next = {value: nums[i]};
        cur = cur.next;
    }
    toDelete.reverse();
    while (toDelete.length) {
        res++;
        for (let node of toDelete) {
            node.next = node.next.next;
        }
        toDelete = toDelete.filter(node => node.next && node.value > node.next.value);
    }
    return res;
};

