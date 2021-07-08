function majorityElement(nums: number[]): number {
    let cnt = 0, target = null;
    for (let num of nums) {
        if (cnt === 0) {
            target = num;
        }
        if (num === target) {
            cnt++;
        } else {
            cnt --;
        }
    }
    cnt = 0;
    for (let num of nums) {
        if (num === target) {
            cnt++;
        }
    }
    return cnt > nums.length / 2 ? target : -1;
};

