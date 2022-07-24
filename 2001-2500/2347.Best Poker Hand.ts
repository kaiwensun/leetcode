function bestHand(ranks: number[], suits: string[]): string {
    function isFlush() {
        for (let i = 1; i < suits.length; i++) {
            if (suits[i] !== suits[i - 1]) {
                return false;
            }
        }
        return true;
    }

    function isSameOfKind(repeat: number) {
        const cnt = {};
        for (const rank of ranks) {
            cnt[rank] ||= 0;
            cnt[rank]++;
        }
        for (const value of Object.values(cnt)) {
            if (value >= repeat) {
                return true;
            }
        }
        return false;
    }

    if (isFlush()) {
        return "Flush";
    } else if (isSameOfKind(3)) {
        return "Three of a Kind";
    } else if (isSameOfKind(2)) {
        return "Pair";
    } else {
        return "High Card";
    }

};

