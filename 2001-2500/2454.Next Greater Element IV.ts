function secondGreaterElement(nums: number[]): number[] {
    const N = nums.length;
    nums.push(Infinity);
    const stack = [N];
    const firstGreaterThan = new Array(N + 1);
    for (let i = 0; i < N + 1; i++) {
        firstGreaterThan[i] = [];
    }
    const answer = new Array(N).fill(-1);

    for (let i = N - 1; i >= 0; i--) {
        const num = nums[i];
        while (num >= nums[stack[stack.length - 1]]) {
            stack.pop();
        }
        const fIndex = stack[stack.length - 1];
        firstGreaterThan[fIndex].push(i);
        stack.push(i);
    }
    firstGreaterThan.forEach(arr => arr.sort((i, j) => nums[i] - nums[j]));

    stack.length = 0;
    stack.push(N)
    for (let k = N - 1; k >= 0; k--) {
        for (let i of firstGreaterThan[k]) {
            while (nums[i] >= nums[stack[stack.length - 1]]) {
                stack.pop();
            }
            if (stack.length > 1) {
                answer[i] = nums[stack[stack.length - 1]];
            }
        }
        while (nums[k] >= nums[stack[stack.length - 1]]) {
            stack.pop();
        }
        stack.push(k)
    }
    return answer;
};

