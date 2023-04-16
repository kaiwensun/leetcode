type Fn = (...params: any) => any

function memoize(fn: Fn): Fn {
    const map = {};
    return function(...args) {
        let p = map;
        for (const arg of args) {
            p = p[arg] ||= {};
        }
        if (p["res"] === undefined) {
            p["res"] = fn(...args);
        }
        return p["res"];
    }
}


/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */

