function checkIfInstanceOf(obj: any, classFunction: any): boolean {
    if (obj === null || obj == undefined) {
        return false;
    }
    if (classFunction === Object) {
        return true;
    }
    let t = Object.getPrototypeOf(obj);
    while (t.constructor !== Object) {
        if (t.constructor === classFunction) {
            return true;
        }
        t = Object.getPrototypeOf(t);
    }
    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */

