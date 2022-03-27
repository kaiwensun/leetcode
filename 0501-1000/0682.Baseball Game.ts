function calPoints(ops: string[]): number {
    const stack = [];
    const operations = {
        "+": () => stack.push(stack[stack.length - 1] + stack[stack.length - 2]),
        D: () => stack.push(stack[stack.length - 1] * 2),
        C: () => stack.pop()
    }
    for (const op of ops) {
        const operation = operations[op] || (x => stack.push(parseInt(x)));
        operation(op);
    }
    return stack.reduce((acc, a) => acc + a, 0);
};

