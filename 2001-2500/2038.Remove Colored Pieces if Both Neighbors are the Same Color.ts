function winnerOfGame(colors: string): boolean {
    const res = {A: 0, B: 0};
    for (let i = 0; i < colors.length; i++) {
        if (i >= 2 && colors[i] == colors[i - 1] && colors[i] == colors[i - 2]) {
            res[colors[i]]++;
        }
    }
    return res.A > res.B;
};

