function chalkReplacer(chalk: number[], k: number): number {
    const sum = chalk.reduce((a, b) => a + b);
    k %= sum;
    for (let i = 0; i < chalk.length; i++) {
        k -= chalk[i];
        if (k < 0) return i;
    }
};

