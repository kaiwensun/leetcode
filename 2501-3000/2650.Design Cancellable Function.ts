function cancellable<T>(generator: Generator<Promise<any>, T, unknown>): [() => void, Promise<T>] {
    let canceled = false;
    function cancel() {
        canceled = true;
    }
    async function handler() {
        let item = generator.next();
        let value;
        while (!item.done) {
            try {
                value = await item.value;
            } catch (e) {
                item = generator.throw(e);
                continue;
            }
            if (canceled) {
                item = generator.throw("Cancelled");
            } else {
                item = generator.next(value);
            }
        }
        return item.value;
    }
    return [cancel, handler()];
};

/**
 * function* tasks() {
 *   const val = yield new Promise(resolve => resolve(2 + 2));
 *   yield new Promise(resolve => setTimeout(resolve, 100));
 *   return val + 1;
 * }
 * const [cancel, promise] = cancellable(tasks());
 * setTimeout(cancel, 50);
 * promise.catch(console.log); // logs "Cancelled" at t=50ms
 */

