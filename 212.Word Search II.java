/**
 *Basic idea:
 * Construct a trie for the dictionary. Remove appropriate branches of trie when a word is found.
 *Result:
 * 37 / 37 test cases passed.
 * Status: Accepted
 * Runtime: 64 ms
 * Your runtime beats 37.41% of java submissions.
 *Date:
 * 10/9/2016
 */
public class Solution {
    private static final Character end = '#';
    private static final char invalid = '-';
    public List<String> findWords(char[][] board, String[] words) {
        HashMap <Character, HashMap> trie = new HashMap<>();
        List<String> res = new LinkedList<>();
        StringBuilder path = new StringBuilder();
        for(String word : words){
            buildDict(trie,word,0);
        }
        for(int r = 0;r<board.length;r++){
            for(int c = 0;c<board[0].length;c++){
                int rtn = searchBoard(board,r,c,trie,res,path);
                if(rtn==0){
                    break;
                }
            }
        }
        return res;
    }
    void buildDict(HashMap<Character,HashMap> trie, String word, int wordIndex){
        if(wordIndex==word.length()){
            trie.put(end,new HashMap<>());
            return;
        }
        Character c = word.charAt(wordIndex);
        if(trie.containsKey(c)){
            buildDict(trie.get(c),word,wordIndex+1);
        }else{
            HashMap map = new HashMap<Character,HashMap>();
            trie.put(c,map);
            buildDict(map,word,wordIndex+1);
        }
    }
    int searchBoard(char[][] board, int r, int c,HashMap<Character, HashMap> trie ,List<String> res, StringBuilder path){
        //System.out.println("Enter searchBoard with ("+r+","+c+")");
        if(trie.containsKey(end)){
            trie.remove(end);
            res.add(path.toString());
            if(trie.size()==0){
                return 0;
            }
        }
        if(r<0 || r>=board.length || c<0 || c>=board[0].length){
            return trie.size();
        }
        char chr = board[r][c];
        HashMap next = trie.get(chr);
        if(next==null){
            //there is no such board word in trie dictionary.
            return trie.size();
        }
        board[r][c] = invalid;
        path.append(chr);
        
        int[] dr = {0,-1,0,1};
        int[] dc = {-1,0,1,0};
        for(int i=0;i<4;i++){
            int rtn = searchBoard(board,r+dr[i],c+dc[i],next,res,path);
            if(rtn==0){
                trie.remove(chr);
                if(trie.size()==0){
                    break;
                }
            }
        }
        path.deleteCharAt(path.length()-1);
        board[r][c] = chr;
        return trie.size();
    }
}
