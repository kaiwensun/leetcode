function largestWordCount(messages: string[], senders: string[]): string {
    const counter: {[k : string] : number} = {};
    for (let i = 0; i < messages.length; i++) {
        counter[senders[i]] ||= 0;
        counter[senders[i]] += messages[i].split(' ').length;
    }
    return Object.keys(counter).sort((a, b) => counter[b] - counter[a] || (a < b ? 1 : -1))[0];
};

