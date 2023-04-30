function isWinner(player1: number[], player2: number[]): number {
    const score1 = getScore(player1);
    const score2 = getScore(player2);
    if (score1 === score2) return 0;
    return score1 > score2 ? 1 : 2;
};

function getScore(player: number[]) {
    let res = 0;
    for (let i = 0; i < player.length; i++) {
        res += player[i];
        if (player[i - 1] === 10 || player[i - 2] === 10) {
            res += player[i];
        }
    }
    return res;
}

