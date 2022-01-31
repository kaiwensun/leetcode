function groupStrings(words: string[]): number[] {

    /* pre-process */
    function toBits(word: string) {
        let res = 0;
        for (const c of word) {
            res |= 1 << (c.charCodeAt(0) - 97);
        }
        return res;
    }

    function groupBits(words: string[]) {
        const group = {};
        for (let i = 0; i <= 27; i++) {
            group[i] = [];
        }
        for (let i = 0; i < words.length; i++) {
            const word = words[i];
            group[word.length].push([toBits(word), i]);
        }
        return group;
    }

    /* union find */
    function find(i) {
        if (UFData[i] !== i) {
            UFData[i] = find(UFData[i]);
        }
        return UFData[i];
    }

    function union(i, j) {
        const ri = find(i);
        const rj = find(j);
        if (ri !== rj) {
            UFData[ri] = rj;
        }
    }

    const UFData = new Array(words.length);
    for (let i = 0; i < words.length; i++) {
        UFData[i] = i;
    }

    /* operations on Union Find */
    function mergeEquivilant(bitArray) {
        const hash = {};
        bitArray.forEach((bits, i) => {
            if (hash.hasOwnProperty(bits)) {
                union(i, hash[bits]);
            } else {
                hash[bits] = i;
            }
        });
        return hash;
    }

    function merge(bitArray, hash) {
        bitArray.forEach((bits, i) => {
            let mask1 = 1;
            for (let j = 0; j < 26; j++) {
                if (hash.hasOwnProperty(bits ^ mask1)) {
                    union(i, hash[bits ^ mask1]);
                }
                if (mask1 & bits) {
                    let mask2 = 1;
                    for (let k = 0; k < 26; k++) {
                        if ((mask2 & bits) === 0) {
                            const mask = mask1 | mask2;
                            if (hash.hasOwnProperty(bits ^ mask)) {
                                union(i, hash[bits ^ mask]);
                            }
                        }
                        mask2 <<= 1;
                    }
                }
                mask1 <<= 1;
            }
        });
    }

    function countUFData() {
        const count = {};
        UFData.forEach(e => {
            count[e] |= 0;
            count[e]++;
        })
        return count;
    }

    function finalizeUF() {
        for (let i = 0; i < UFData.length; i++) {
            find(i);
        }
    }

    const bitArray = words.map(word => toBits(word));
    const hash = mergeEquivilant(bitArray);
    mergeEquivilant(bitArray);
    merge(bitArray, hash);
    finalizeUF();
    const count = countUFData();

    return [Object.keys(count).length, Math.max(...Object.values(count) as number[])]
};

