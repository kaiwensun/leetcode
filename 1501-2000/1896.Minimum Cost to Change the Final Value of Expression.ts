function minOperationsToFlip(exp: string): number {
    type Node = {
        value: number;
        op?: string;
        left?: Node;
        right?: Node;
        minCost?: [number, number]
    }

    const parse = (i: number): [Node, number] => {
        let value: number, right: Node, left: Node, new_i: number, op: string;
        new_i = i;
        console.assert('01)'.includes(exp[i]));
        if (exp[i] === ')') {
            [right, new_i] = parse(i - 1);
            console.assert(exp[new_i] === '(');
        } else {
            right = { value: +exp[i] };
        }
        new_i--;
        console.assert(new_i === -1 || '|&('.includes(exp[new_i]), new_i);
        if (new_i === -1 || exp[new_i] === '(') {
            return [right, new_i];
        }
        op = exp[new_i--];
        console.assert("|&".includes(op));
        [left, new_i] = parse(new_i);
        return [{
            value: eval(left.value + op + right.value),
            op, left, right
        }, new_i];
    }

    const minCost = (node: Node, wanted: number): number => {
        node.minCost ||= [undefined, undefined];
        if (node.minCost[wanted] !== undefined) {
            return node.minCost[wanted];
        }
        let cost = Infinity;
        if (node.value === wanted) {
            cost = 0;
        } else if (node.op === undefined) {
            cost = 1;
        } else {
            // cost if we do not flip operator
            if ((node.op === "|") === (wanted === 0)) {
                cost = Math.min(
                    minCost(node.left, wanted) + minCost(node.right, wanted),
                    1 + Math.min(minCost(node.left, wanted), minCost(node.right, wanted))
                );
            } else {
                cost = Math.min(
                    Math.min(minCost(node.left, wanted), minCost(node.right, wanted)),
                    1 + minCost(node.left, wanted) + minCost(node.right, wanted)
                );
            }
        }
        node.minCost[wanted] = cost;
        return cost;

    }
    let [tree, new_i] = parse(exp.length - 1);
    console.assert(new_i === -1);
    return minCost(tree, 1 - tree.value);
};

