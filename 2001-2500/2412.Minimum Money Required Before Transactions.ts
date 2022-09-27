function minimumMoney(transactions: number[][]): number {
    const total = transactions.reduce((acc, [cost, cashback]) => acc + Math.max(0, cost - cashback), 0);
    const maxReduce = transactions.filter(([cost, cashback]) => cost >= cashback).reduce((acc, [_, cashback]) => Math.max(acc, cashback), 0);
    const maxJump = transactions.filter(([cost, cashback]) => cost < cashback).reduce((acc, [cost, _]) => Math.max(acc, cost), 0);
    return total + Math.max(maxJump, maxReduce);
};

