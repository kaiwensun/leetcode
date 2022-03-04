function subArrayRanges(nums: number[]): number {
    const N = nums.length;
    function sumMinimum(nums: number[]) {
        const leftBound = Array();
        const rightBound = Array();
        nums[-1] = nums[N] = -Infinity;
        const stack = [-1];
        for (let i = 0; i < N; i++) {
            while (nums[stack[stack.length - 1]] > nums[i]) {
                stack.pop();
            }
            leftBound[i] = stack[stack.length - 1];
            stack.push(i);
        }
        stack.length = 1;
        for (let i = N - 1; i >= 0; i--) {
            while (nums[stack[stack.length - 1]] >= nums[i]) {
                stack.pop();
            }
            rightBound[i] = stack[stack.length - 1] == -1 ? N : stack[stack.length - 1];
            stack.push(i);
        }
        let sum = 0;
        for (let i = 0; i < N; i++) {
            sum += (rightBound[i] - i) * (i - leftBound[i]) * nums[i];
        }
        return sum;
    }
    const minSum = sumMinimum(nums);
    const maxSum = -sumMinimum(nums.map(num => -num));
    return maxSum - minSum;
};

