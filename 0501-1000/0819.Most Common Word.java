class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> bannedSet = new HashSet<>(Arrays.stream(banned).map(word -> word.toLowerCase()).collect(Collectors.toSet()));
        bannedSet.add("");
        Map<String, Integer> counter = new HashMap<>();
        for (String word : paragraph.split("[ !?',;.]")) {
            word = word.toLowerCase();
            counter.put(word, counter.getOrDefault(word, 0) - 1);
        }
        return counter.entrySet().stream()
            .filter(entry -> !bannedSet.contains(entry.getKey()))
            .sorted(Map.Entry.comparingByValue())
            .findFirst().get().getKey();
    }
}

