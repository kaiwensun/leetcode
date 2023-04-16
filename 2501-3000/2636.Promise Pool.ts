type F = () => Promise<any>;

function promisePool(functions: F[], n: number): Promise<any> {
    const wrappers = functions.map((f, i) => async () => {
        await f();
        if (remainings.length) {
            const remaining = remainings.shift();
            await remaining();
        }
    });
    const pendings = wrappers.slice(0, n);
    const remainings = wrappers.slice(n);
    return Promise.all(pendings.map(pending => pending()));
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */

