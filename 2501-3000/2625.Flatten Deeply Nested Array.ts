type MultiDimensionalArray = (number | MultiDimensionalArray)[];

var flat = function (arr:  MultiDimensionalArray, n: number):  MultiDimensionalArray {
    if (n <= 0) {
        return arr;
    }
    let res = [];
    for (const item of arr) {
        if (typeof item === 'number') {
            res.push(item);
        } else {
            for (const child of flat(item, n - 1)) {
                res.push(child);
            }
        }
    }
    return res;
};

