class ATM {
    
    private readonly notes = [20, 50, 100, 200, 500];
    private count = new Array(this.notes.length).fill(0);
    constructor() {
    }

    deposit(banknotesCount: number[]): void {
        for (let i = 0; i < this.notes.length; i++) {
            this.count[i] += banknotesCount[i];
        }
    }

    withdraw(amount: number): number[] {
        if (amount % 10) return [-1];
        const res = new Array(this.notes.length).fill(0);
        for (let i = this.notes.length - 1; i >= 0; i--) {
            const take = Math.min(Math.floor(amount / this.notes[i]), this.count[i]);
            this.count[i] -= take;
            res[i] = take;
            amount -= this.notes[i] * take;
        }
        if (amount > 0) {
            this.deposit(res);
            return [-1];
        }
        return res;
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * var obj = new ATM()
 * obj.deposit(banknotesCount)
 * var param_2 = obj.withdraw(amount)
 */

