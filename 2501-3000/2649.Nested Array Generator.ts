type MultidimensionalArray = (MultidimensionalArray | number)[]

function* inorderTraversal(arr: MultidimensionalArray): Generator<number, void, unknown> {
    for (const item of arr) {
        if (typeof item === 'number') {
            yield item;
        } else {
            for (const num of inorderTraversal(item)) {
                yield num;
            }
        }
    }
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */

