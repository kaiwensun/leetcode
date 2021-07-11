function sumGame(num: string): boolean {
    const N = num.length;
    let lStr = num.slice(0, N / 2), rStr = num.slice(N / 2);
    let lInt = lStr.split('').map(d => parseInt(d)).filter(d => !isNaN(d));
    let rInt = rStr.split('').map(d => parseInt(d)).filter(d => !isNaN(d));
    let qDiff = rInt.length - lInt.length;
    let sumDiff = lInt.reduce((a, b) => a + b, 0) - rInt.reduce((a, b) => a + b, 0);
    if (qDiff === 0) {
        return sumDiff !== 0;
    }
    if (qDiff % 2) {
        return true;
    }
    if (qDiff < 0) {
        const tmpStr = lStr; lStr = rStr; rStr = tmpStr;
        const tmpInt = lInt; lInt = rInt; rInt = tmpInt;
        qDiff = -qDiff;
        sumDiff = -sumDiff;
    }
    if (sumDiff > 0) {
        return true;
    } else if (sumDiff === 0) {
        return false;
    } else {
        return 9 * (qDiff / 2) + sumDiff !== 0;
    }
};

