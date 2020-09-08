class Solution {
    public boolean pyramidTransition(String bottom, List<String> allowed) {
        if (bottom.length() <= 1) {
            return true;
        }
        Set<Integer>[][] allowedDict = buildAllowed(allowed);
        int[][] blocks = buildBlocks(bottom);
        return fillCell(blocks, allowedDict, 1, 0);
    }
    private boolean fillCell(int[][] blocks, Set<Integer>[][] allowedDict, int row, int col) {
        int left = blocks[row - 1][col];
        int right = blocks[row - 1][col + 1];
        Set<Integer> possibleBlocks = allowedDict[left][right];
        if (possibleBlocks.isEmpty()) {
            return false;
        } else {
            if (row == blocks.length - 1) {
                return true;
            }
            int nextCol = col + 1;
            int nextRow = row;
            if (nextCol >= blocks[nextRow].length) {
                ++nextRow;
                nextCol = 0;
            }
            for (int possibleBlock : possibleBlocks) {
                blocks[row][col] = possibleBlock;
                if (fillCell(blocks, allowedDict, nextRow, nextCol)) {
                    return true;
                }
            }
        }
        return false;
    }
    private int[][] buildBlocks(String bottom) {
        int size = bottom.length();
        int[][] blocks = new int[size][];
        for (int i = 0; i < size; ++i) {
            blocks[i] = new int[size - i];
        }
        for (int i = 0; i < bottom.length(); ++i) {
            blocks[0][i] = bottom.charAt(i) - 'A';
        }
        return blocks;
    }
    private Set<Integer>[][] buildAllowed(List<String> allowed) {
        final int dictSize = 7;
        Set<Integer>[][] allowedDict = new Set[dictSize][];
        for (int i = 0; i < dictSize; ++i) {
            allowedDict[i] = new Set[dictSize];
            for (int j = 0; j < dictSize; ++j) {
                allowedDict[i][j] = new HashSet<>();
            }
        }
        for (String oneAllowed : allowed) {
            allowedDict[oneAllowed.charAt(0) - 'A'][oneAllowed.charAt(1) - 'A'].add(oneAllowed.charAt(2) - 'A');
        }
        return allowedDict;
    }
}

