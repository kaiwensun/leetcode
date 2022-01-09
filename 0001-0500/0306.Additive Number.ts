function isAdditiveNumber(num: string): boolean {
    function test(num1: number, num2: number, startIndex: number) {
        if (startIndex == num.length) {
            return true;
        }
        if (startIndex > num.length) {
            return false;
        }
        const str = `${num1 + num2}`;
        if (startIndex + str.length > num.length) {
            return false;
        }
        for (let i = 0; i < str.length; i++) {
            if (num[startIndex + i] !== str[i]) {
                return false;
            }
        }
        return test(num2, parseInt(str), startIndex + str.length);
    }
    for (let size1 = 1; size1 < num.length / 2; size1++) {
        if (num[0] === '0' && size1 > 1) {
            break;
        }
        for (let size2 = 1; size2 < num.length / 2 && Math.max(size1, size2) * 2 < num.length; size2++) {
            if (num[size1] === '0' && size2 > 1) {
                break;
            }
            if (test(parseInt(num.substr(0, size1)), parseInt(num.substr(size1, size2)), size1 + size2)) {
                return true;
            }
        }
    }
    return false;
};

