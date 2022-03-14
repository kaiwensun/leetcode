function findRestaurant(list1: string[], list2: string[]): string[] {
    const map1 = {}, map2 = {};
    list1.forEach((value, index) => {map1[value] = index});
    list2.forEach((value, index) => {map2[value] = index});
    let minSum = Infinity;
    const res = [];
    list1.filter(rest => map2[rest] !== undefined).forEach(rest => {
        const sum = map1[rest] + map2[rest];
        if (sum === minSum) {
            res.push(rest);
        } else if (sum < minSum) {
            res.length = 0;
            minSum = sum;
            res.push(rest);
        }
    })
    return res;
};

