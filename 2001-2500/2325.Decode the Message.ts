function decodeMessage(key: string, message: string): string {
    const map = {' ': ' '};
    let i = 97;
    for (let c of key) {
        if (!map[c]) {
            map[c] = String.fromCharCode(i++);
        }
    }
    return [...message].map(c => map[c] || c).join('');
};

