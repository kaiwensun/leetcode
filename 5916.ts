function minimumOperations(nums: number[], start: number, goal: number): number {
    if (start === goal) {
        return 0;
    }
    const reached = Array(1001).fill(false);
    reached[start] = true;
    const queue = [start, undefined];
    let step = 1;
    while (queue.length > 1) {
        const item = queue.shift();
        if (item === undefined) {
            step++;
            queue.push(item);
            continue;
        }
        for (const num of nums) {
            for (const nxt of [item + num, item - num, item ^ num]) {
                if (nxt === goal) {
                    return step;
                }
                if (0 <= nxt && nxt <= 1000) {
                    if (!reached[nxt]) {
                        reached[nxt] = true;
                        queue.push(nxt);
                    }
                }
            }
        }
    }
    return -1;
};

