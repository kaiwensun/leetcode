var row1str = "qwertyuiopQWERTYUIOP";
var row2str = "asdfghjklASDFGHJKL";
var row3str = "zxcvbnmZXCVBNM";
var row1Obj = convert2Map(row1str);
var row2Obj = convert2Map(row2str);
var row3Obj = convert2Map(row3str);
function convert2Map(str){
    var obj = {};
    for(var i = 0;i<str.length;i++){
        obj[str.charAt(i)]=i;
    }
    return obj;
}
function getGroup(c){
    switch(true){
        case c in row1Obj: return 1;
        case c in row2Obj: return 2;
        case c in row3Obj: return 3;
        default: return -1;
    }
}
function isInOneRow(word){
    if(word.length!==0){
        var group = getGroup(word.charAt(0));
        for(var i=1;i<word.length;i++){
            if(getGroup(word.charAt(i))!=group){
                return false;
            }
        }
    }
    return true;
}
var findWords = function(words) {
    return words.filter(isInOneRow);
};


// =================================trying another syntax========================
var row1str = "qwertyuiopQWERTYUIOP";
var row2str = "asdfghjklASDFGHJKL";
var row3str = "zxcvbnmZXCVBNM";
var row1Obj = convert2Map(row1str);
var row2Obj = convert2Map(row2str);
var row3Obj = convert2Map(row3str);
function convert2Map(str){
    var obj = {};
    for(var i = 0;i<str.length;i++){
        obj[str.charAt(i)]=i;
    }
    return obj;
}
function getGroup(c){
    switch(true){
        case c in row1Obj: return 1;
        case c in row2Obj: return 2;
        case c in row3Obj: return 3;
        default: return -1;
    }
}
function isInOneRow(word){
    if(word.length===0){
        return true;
    }
    var groups = word.split("").map(getGroup);
    return groups.reduce(function(res,group){return res&&(group===groups[0])},true);
}
var findWords = function(words) {
    return words.filter(isInOneRow);
};
