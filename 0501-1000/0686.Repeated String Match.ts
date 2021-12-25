function repeatedStringMatch(a: string, b: string): number {
    let repeat = Math.ceil(b.length * 2 / a.length);
    const aa = a.repeat(Math.max(repeat, 2));
    const i = aa.indexOf(b);
    if (i === -1) {
        return -1;
    }
    return Math.ceil((i + b.length) / a.length);
};

