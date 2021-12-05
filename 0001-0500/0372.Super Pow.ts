const MOD = 1337;

function superPow(a: number, b: number[]): number {
    function compressB(b: number[], loop: number) {
        const loop_digits = ('' + loop).length;
        while (b.length > loop_digits) {
            let bnum = 0;
            for (let i = 0; i < loop_digits + 1; i++) {
                bnum *= 10;
                bnum += b.shift();
            }
            bnum %= loop;
            while (bnum) {
                b.unshift(bnum % 10);
                bnum -= bnum % 10;
                bnum /= 10;
            }
        }
        return b.length === 0 ? 0 : parseInt(b.join('')) % loop;
    }
    
    a %= MOD;
    let cur = a;
    const seen = new Set();
    const track = [];
    while (!seen.has(cur)) {
        seen.add(cur);
        track.push(cur);
        cur *= a;
        cur %= MOD;
    }
    const bnum = compressB(b, track.length);
    return track[(bnum + track.length - 1) % track.length];
};

