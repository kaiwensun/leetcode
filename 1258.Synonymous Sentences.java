// import java.util.stream.Collectors; 

class Solution {
    class UnionFind {
        
        private Map<String, Set<String>> dictionary = new HashMap<>();
        private Map<String, String> parents = new HashMap<>();
        public String find(String w) {
            String parent = parents.get(w);
            if (parent == null) {
                parents.put(w, w);
                Set<String> set = new HashSet<>();
                set.add(w);
                dictionary.put(w, set);
                return w;
            } else if (w.equals(parent)) {
                return w;
            } else {
                parents.put(w, find(parent));
                return parents.get(w);
            }
        }
        public void union(String w1, String w2) {
            String p1 = find(w1);
            String p2 = find(w2);
            if (!p1.equals(p2)) {
                parents.put(p1, p2);
                dictionary.get(p2).addAll(dictionary.get(p1));
                dictionary.put(p1, dictionary.get(p2));
            }
        }
        public Set<String> getSynonyms(String w) {
            return dictionary.get(find(w));
        }
    }
    public List<String> generateSentences(List<List<String>> synonyms, String text) {
        UnionFind uf = new UnionFind();
        for (List<String> pair : synonyms) {
            String w1 = pair.get(0);
            String w2 = pair.get(1);
            uf.union(w1, w2);
        }
        
        String[] sentence = text.split(" ");
        List<String> collector = new ArrayList<>();
        collector.add(new String());
        for (String word : sentence) {
            Set<String> synonymous = uf.getSynonyms(word);
            ArrayList<String> sortedSynonymous = new ArrayList<String>(synonymous);
            Collections.sort(sortedSynonymous);
            List<String> newCollector = new ArrayList<>();
            for (String prefix : collector) {
                for (String syn : sortedSynonymous) {
                    newCollector.add((prefix.length() == 0 ? prefix : prefix + " ") + syn);
                }
            }
            collector = newCollector;
        }
        return collector;
    }
}
