public class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        int startId = 0;
        List<String> res = new LinkedList<>();
        while(startId<words.length){
            int[] id_len = getNextIndexAndLen(words, maxWidth, startId);
            if(id_len==null){
                return null;
            }
            
            System.out.println(id_len[0]+","+id_len[1]);
            int endId = id_len[0];
            if(endId!=words.length-1){
                res.add(fillOneLine(words, maxWidth, startId, endId, id_len[1]));
            }else{
                res.add(fillLastLine(words, maxWidth, startId, endId, id_len[1]));
            }
            startId = endId+1;
        }
        return res;
    }
    
    private String fillLastLine(String[] words, int maxWidth, int startId, int endId, int totalLen){
        StringBuilder sb = new StringBuilder(words[startId]);
        for(int i=startId+1;i<=endId;i++){
            sb.append(" ");
            sb.append(words[i]);
        }
        while(sb.length()<maxWidth){
            sb.append(" ");
        }
        return sb.toString();
    }
    private String fillOneLine(String[] words, int maxWidth, int startId, int endId, int totalLen){
        StringBuilder sb = new StringBuilder(words[startId]);
        if(endId==startId){//only one word in a line
            while(sb.length()<maxWidth){
                sb.append(" ");
            }
        }else{
            int rest = maxWidth-totalLen;
            int sizeOfSpace = rest/(endId-startId)+1;
            int numOfOneMore = rest%(endId-startId);
            String spaces = getSpaces(sizeOfSpace);
            for(int i=startId+1;i<=endId;i++){
                sb.append(spaces);
                if(i-startId<=numOfOneMore){
                    sb.append(" ");
                }
                sb.append(words[i]);
            }
        }
        return sb.toString();
    }
    private String getSpaces(int num){
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<num;i++){
            sb.append(" ");
        }
        return sb.toString();
    }
    /**
     * return {index of the last word, total len}
     */
    private int[] getNextIndexAndLen(String[] words, int maxWidth, int startId){
        int totalLen = 0;
        int i=startId;
        while(i<words.length){
            if(words[i].length()>maxWidth){
                return null;
            }
            totalLen += words[i].length();
            if(totalLen>maxWidth){
                totalLen -= words[i].length();
                break;
            }
            if(totalLen>=maxWidth-1){
                i+=1;
                totalLen+=1;
                break;
            }
            totalLen+=1;
            i++;
        }
        return new int[]{i-1, totalLen-1};
    }
}
