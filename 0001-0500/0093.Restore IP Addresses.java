class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> result = new ArrayList<>();
        List<String> stack = new ArrayList<>();
        dfs(s, 0, stack, result);
        return result;
    }

    private void dfs(String s, int i, List<String> stack, List<String> acc) {
        if (stack.size() == 4) {
            if (i == s.length()) {
                acc.add(String.join(".", stack));
            }
            return;
        }
        if (i >= s.length()) {
            return;
        }
        stack.add(s.substring(i, i + 1));
        dfs(s, i + 1, stack, acc);
        stack.remove(stack.size() - 1);

        if (s.charAt(i) != '0') {
            if (i + 1 < s.length()) {
                stack.add(s.substring(i, i + 2));
                dfs(s, i + 2, stack, acc);
                stack.remove(stack.size() - 1);
            }
            if (i + 2 < s.length() && s.substring(i, i + 3).compareTo("256") < 0) {
                stack.add(s.substring(i, i + 3));
                dfs(s, i + 3, stack, acc);
                stack.remove(stack.size() - 1);
            }
        }
    }
}

