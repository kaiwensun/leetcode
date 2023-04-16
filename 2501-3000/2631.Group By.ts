declare global {
    interface Array<T> {
        groupBy(fn: (item: T) => string): Record<string, T[]>
    }
}

Array.prototype.groupBy = function(fn) {
    const res = {};
    this.forEach(item => {
        const key = fn(item);
        res[key] ||= [];
        res[key].push(item);
    });
    return res;
}

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */

