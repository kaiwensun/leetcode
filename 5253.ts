function kthPalindrome(queries: number[], intLength: number): number[] {
    return queries.map(q => {
        let res = '';
        if (intLength === 1) {
            res = "" + q;
        } else if (intLength % 2 === 0) {
            const base = 10 ** (Math.floor(intLength / 2) - 1);
            const half = base + q - 1;
            res = half + ("" + half).split('').reverse().join('');
        } else {
            const base = 10 ** (Math.floor(intLength / 2) - 1);
            const half = base + Math.floor((q - 1) / 10);
            const mid = (q - 1) % 10;
            res = '' + half + mid + ("" + half).split('').reverse().join('');
        }
        return res.length === intLength ? parseInt(res) : -1;
    });
};

