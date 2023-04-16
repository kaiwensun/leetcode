function curry(fn: Function): Function {
    return function curried(...args1) {
        if (fn.length === args1.length) {
            return fn(...args1);
        } else {
            return (...args2) => curried.apply(this, args1.concat(args2));
        }
    };
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */

