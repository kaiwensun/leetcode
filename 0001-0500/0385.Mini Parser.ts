/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *     If value is provided, then it holds a single integer
 *     Otherwise it holds an empty nested list
 *     constructor(value?: number) {
 *         ...
 *     };
 *
 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     isInteger(): boolean {
 *         ...
 *     };
 *
 *     Return the single integer that this NestedInteger holds, if it holds a single integer
 *     Return null if this NestedInteger holds a nested list
 *     getInteger(): number | null {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a single integer equal to value.
 *     setInteger(value: number) {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
 *     add(elem: NestedInteger) {
 *         ...
 *     };
 *
 *     Return the nested list that this NestedInteger holds,
 *     or an empty list if this NestedInteger holds a single integer
 *     getList(): NestedInteger[] {
 *         ...
 *     };
 * };
 */

function deserialize(s: string): NestedInteger {

    function* tokenizer(s: string) {
        let numStr: string = "";
        for (let i = 0; i < s.length; i++) {
            if ("[],".includes(s[i])) {
                if (numStr.length) {
                    yield numStr;
                    numStr = "";
                }
                yield s[i];
            } else {
                numStr += s[i];
            }
        }
        if (numStr.length) {
            yield numStr;
        }
    }

    const tokens = tokenizer(s);
    function aggregator(tokens) {
        const res = new NestedInteger();
        let token = tokens.next().value;
        if (token === "[") {
            while (token !== "]") {
                const child = aggregator(tokens);
                if (child) {
                    res.add(child);
                    token = tokens.next().value;
                } else {
                    break;
                }
            }
        } else if (token === "]") {
            return undefined;
        } else {
            res.setInteger(parseInt(token));
        }
        return res;
    }
    return aggregator(tokens);
};

