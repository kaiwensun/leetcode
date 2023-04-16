type F = (x: number) => number;

function compose(functions: F[]): F {
	return function(x) {
        return functions.reverse().reduce((acc, f) => f(acc), x);
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */

