function twoSum(numbers: number[], target: number): number[] {
    let l = 0, r = numbers.length - 1;
    while (l < r) {
        const sum = numbers[l] + numbers[r];
        if (sum === target) {
            return [l, r];
        } else if (sum < target) {
            l++;
        } else {
            r--;
        }
    }
    throw "input constraint violated";
};

