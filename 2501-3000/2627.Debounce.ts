type F = (...p: any[]) => any

function debounce(fn: F, t: number): F {
    let lastTime;
    return function(...args) {
        const time = new Date();
        lastTime = time;
        setTimeout(() => {
            if (time === lastTime) {
                return fn(...args);
            }
        }, t);
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */

