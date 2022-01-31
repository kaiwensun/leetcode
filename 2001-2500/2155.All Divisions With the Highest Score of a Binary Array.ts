function maxScoreIndices(nums: number[]): number[] {
    let left = 0, right = nums.filter(num => num).length, max = right, res = [0];
    nums.forEach((num, i) => {
        if (num) {
            right--;
        } else {
            left++;
        }
        if (left + right > max) {
            max = left + right;
            res.length = 0;
        }
        if (left + right === max) {
            res.push(i + 1);
        }
    });
    return res;
};

