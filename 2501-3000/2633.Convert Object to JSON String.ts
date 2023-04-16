function jsonStringify(object: any): string {
    if (Array.isArray(object)) {
        return jsonfyArray(object);
    } else if (typeof object === "object" && object !== null) {
        return jsonfyObject(object);
    } else if (typeof object === "string") {
        return `"${object}"`;
    } else {
        return `${object}`;
    }
};
function jsonfyArray(array: any[]) {
    return `[${array.map(obj => jsonStringify(obj)).join(",")}]`;
}
function jsonfyObject(object: Object) {
    return `{${Object.keys(object).map(key => `"${key}":${jsonStringify(object[key])}`).join(",")}}`;
}

