class Solution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        Arrays.sort(players);
        Arrays.sort(trainers);
        int j = 0, res = 0;
        for (int player : players) {
            while (j < trainers.length && player > trainers[j]) {
                j++;
            }
            if (j++ < trainers.length) {
                res++;
            } else {
                break;
            }
            
        }
        return res;
    }
}

