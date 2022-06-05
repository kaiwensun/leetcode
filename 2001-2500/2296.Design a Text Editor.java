class TextEditor {
    private ListIterator<Character> iter;

    public TextEditor() {
        iter = new LinkedList<Character>().listIterator();
    }
    
    public void addText(String text) {
        for (char c : text.toCharArray()) {
            iter.add(c);
        }
    }

    public int deleteText(int k) {
        int res = 0;
        for (int i = 0; i < k && iter.hasPrevious(); i++) {
            res++;
            iter.previous();
            iter.remove();
        }
        return res;
    }
    
    public String cursorLeft(int k) {
        for (int i = 0; i < k && iter.hasPrevious(); i++) {
            iter.previous();
        }
        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        for (int i = 0; i < 10 && iter.hasPrevious(); i++, cnt++) {
            sb.append(iter.previous());
        }
        for (int i = 0; i < cnt; i++) {
            iter.next();
        }
        return sb.reverse().toString();
    }
    
    public String cursorRight(int k) {
        for (int i = 0; i < k && iter.hasNext(); i++) {
            iter.next();
        }
        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        for (int i = 0; i < 10 && iter.hasPrevious(); i++, cnt++) {
            sb.append(iter.previous());
        }
        for (int i = 0; i < cnt; i++) {
            iter.next();
        }
        return sb.reverse().toString();
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor obj = new TextEditor();
 * obj.addText(text);
 * int param_2 = obj.deleteText(k);
 * String param_3 = obj.cursorLeft(k);
 * String param_4 = obj.cursorRight(k);
 */

