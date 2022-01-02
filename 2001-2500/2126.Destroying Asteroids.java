class Solution {
    public boolean asteroidsDestroyed(long mass, int[] asteroids) {
        Arrays.sort(asteroids);
        for (int asteroid : asteroids) {
            if (mass >= asteroid) {
                mass += asteroid;
            } else {
                return false;
            }
        }
        return true;
    }
}

