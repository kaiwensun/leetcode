function decodeCiphertext(encodedText: string, rows: number): string {
    const table = [];
    const cols = encodedText.length / rows;
    for (let i = 0; i < encodedText.length; i += cols) {
        table.push(encodedText.substr(i, i + cols));
    }
    let i = 0, j = 0;
    const res = [];
    while (j !== (table[0]?.length || 0)) {
        res.push(table[i++][j++]);
        if (i == rows) {
            i = 0;
            j -= rows - 1;
        }
    }
    return res.join('').trimEnd();
};

