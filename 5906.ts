const reg = /^([a-z]+(-?[a-z]+)?)?[!,.]?$/;

function countValidWords(sentence: string): number {
    return sentence.match(/\S+/g).filter(word => reg.test(word)).length;
};

