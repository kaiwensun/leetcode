function maximumEvenSplit(finalSum: number): number[] {
    if (finalSum % 2 != 0) {
        return [];
    }
    const res = [];
    let num = 0;
    while (finalSum > 0) {
        num += 2;
        finalSum -= num;
        res.push(num);
    }
    if (finalSum < 0) {
        res.push(res.pop() + res.pop() + finalSum);
    }
    return res;
};

