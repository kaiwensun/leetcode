function areDeeplyEqual(o1: any, o2: any): boolean {
    if (getType(o1) !== getType(o2)) {
        return false;
    }
    if ((o1 === null)) {
        return o1 === o2;
    }
    if (Array.isArray(o1)) {
        if (o1.length !== o2.length) {
            return false;
        }
        for (let i = 0; i < o1.length; i++) {
            if (!areDeeplyEqual(o1[i], o2[i])) {
                return false;
            }
        }
        return true;
    }
    if (typeof o1 === "object") {
        if (!areDeeplyEqual(Object.keys(o1).sort(), Object.keys(o2).sort())) {
            return false;
        }
        for (let key of Object.keys(o1)) {
            if (!areDeeplyEqual(o1[key], o2[key])) {
                return false;
            }
        }
        return true;
    }
    return o1 === o2;
};

function getType(obj) {
    if (obj === null) {
        return "null";
    }
    if (Array.isArray(obj)) {
        return "array";
    }
    return typeof obj;
}

