function halveArray(nums: number[]): number {
    const half = nums.reduce((acc, num) => acc + num, 0) / 2;
    let sum = half * 2;
    const heap = new MaxPriorityQueue({priority: a => a});
    nums.forEach(num => heap.enqueue(num));
    let res = 0;
    while (sum > half) {
        const num = heap.dequeue().element / 2;
        sum -= num;
        heap.enqueue(num);
        res++;
    };
    return res;
};

