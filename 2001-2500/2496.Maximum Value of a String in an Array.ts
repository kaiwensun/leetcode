function maximumValue(strs: string[]): number {
    return strs.reduce((acc, str) => Math.max(acc, [...str].filter(c => '0' > c || c > '9').length ? str.length : parseInt(str)), -Infinity);
};

