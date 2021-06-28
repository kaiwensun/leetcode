/**
 * @param {number[][]} routes
 * @param {number} source
 * @param {number} target
 * @return {number}
 */
var numBusesToDestination = function(routes, source, target) {
    if (source === target) {
        return 0;
    }
    const stop2route = {};
    routes.forEach((route, routeId) => {
        route.forEach(stop => {
            stop2route[stop] ||= [];
            stop2route[stop].push(routeId)
        })
    });
    const visited = new Set();
    const queue = stop2route[source].concat(["#"]);
    let res = 0;
    while (queue.length > 1) {
        let routeId = queue.shift();
        if (routeId === "#") {
            res ++;
            queue.push(routeId);
            continue;
        }
        for (let stop of routes[routeId]) {
            if (stop === target) {
                return res + 1;
            }
            stop2route[stop].forEach(nextRoute => {
                if (!visited.has(nextRoute)) {
                    visited.add(nextRoute)
                    queue.push(nextRoute);
                }
            });
        }
    }
    return -1;
};

