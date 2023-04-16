type Fn = (...params: any[]) => Promise<any>;

function timeLimit(fn: Fn, t: number): Fn {
    const timer = async () => {
        await new Promise(res => setTimeout(res, t));
        throw "Time Limit Exceeded";
    }
	return async function(...args) {
        return Promise.race([timer(), fn(...args)]);
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */

