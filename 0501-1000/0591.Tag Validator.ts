function isValid(code: string): boolean {
    if (!code.startsWith("<") || !code.endsWith(">") || code.startsWith("<!")) return false;
    const tags = [];
    let curTag = [];
    let isInCdata = 0;
    for (let i = 0; i < code.length; i++) {
        const c = code[i];
        if (isInCdata) {
            if (c !== "]]>"[3 - isInCdata--]) {
                isInCdata = 3;
            }
        } else if (c === '<') {
            if (curTag.length) return false;
            curTag.push('<');
        } else if (c === '>' && curTag.length) {
            if (curTag[1] === '/') {
                const tag = curTag.slice(2).join("");
                if (!tags.length || tags[tags.length - 1] !== tag) {
                    return false;
                }
                tags.pop();
                curTag.length = 0;
                if (tags.length === 0 && i !== code.length - 1) {
                    return false;
                }
            } else {
                if (curTag.length > 10 || curTag.length === 1 || curTag.slice(1).filter(a => a < 'A' || a > 'Z').length) {
                    return false;
                }
                tags.push(curTag.slice(1).join(""));
                curTag.length = 0;
            }
        } else if (curTag.length) {
            curTag.push(c);
            if (curTag.length === 9 && curTag.join("") === "<![CDATA[") {
                isInCdata = 3;
                curTag.length = 0;
            }
        }
    }
    return curTag.length === 0 && tags.length === 0 && isInCdata === 0;
};

