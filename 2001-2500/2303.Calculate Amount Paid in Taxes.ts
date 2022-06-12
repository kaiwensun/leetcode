function calculateTax(brackets: number[][], income: number): number {
    let prev = [0, 0];
    let res = 0
    for (const bracket of brackets) {
        res += (Math.min(income, bracket[0]) - prev[0]) * bracket[1]
        if (income <= bracket[0]) {
            break;
        }
        prev = bracket;
    }
    return res / 100;
};

