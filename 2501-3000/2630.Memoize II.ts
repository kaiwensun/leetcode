type Fn = (...params: any) => any

function memoize(fn: Fn): Fn {
    const cache = {};
    return function() {
        let map = cache[arguments.length] ||= new Map();
        let exist = true;
        if (!map.has(fn)) {
            exist = false;
            map.set(fn, new Map());
        }
        map = map.get(fn);
        for (const arg of arguments) {
            if (!map.has(arg)) {
                exist = false;
                map.set(arg, new Map);
            }
            map = map.get(arg);
        }
        if (!exist) {
            map.set(0, fn(...arguments));
        }
        return map.get(0);
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

