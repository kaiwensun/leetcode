import java.awt.Point;

class DetectSquares {
    Map<Point, Integer> cnt;
    Map<Integer, Set<Point>> interceptToPoints1;
    Map<Integer, Set<Point>> interceptToPoints2;

    private Point wrap(int[] point) {
        return new Point(point[0], point[1]);
    }

    public DetectSquares() {
        cnt = new HashMap<>();
        interceptToPoints1 = new HashMap<>();
        interceptToPoints2 = new HashMap<>();
    }

    public void add(int[] p) {
        Point point = wrap(p);
        cnt.put(point, cnt.getOrDefault(point, 0) + 1);

        int intercept1 = point.y - point.x;
        Set points = interceptToPoints1.getOrDefault(intercept1, new HashSet());
        points.add(point);
        interceptToPoints1.put(intercept1, points);

        int intercept2 = point.y + point.x;
        points = interceptToPoints2.getOrDefault(intercept2, new HashSet());
        points.add(point);
        interceptToPoints2.put(intercept2, points);
    }

    public int count(int[] p) {
        Point point = wrap(p);
        int res = 0;

        int intercept1 = point.y - point.x;
        for (Point point2 : interceptToPoints1.getOrDefault(intercept1, new HashSet<>())) {
            if (point2.x == point.x) continue;
            int cnt1 = cnt.get(point2);
            int cnt2 = cnt.getOrDefault(new Point(point.x, point2.y), 0);
            int cnt3 = cnt.getOrDefault(new Point(point2.x, point.y), 0);
            res += cnt1 * cnt2 * cnt3;
        }

        int intercept2 = point.y + point.x;
        for (Point point2 : interceptToPoints2.getOrDefault(intercept2, new HashSet<>())) {
            if (point2.x == point.x) continue;
            int cnt1 = cnt.get(point2);
            int cnt2 = cnt.getOrDefault(new Point(point.x, point2.y), 0);
            int cnt3 = cnt.getOrDefault(new Point(point2.x, point.y), 0);
            res += cnt1 * cnt2 * cnt3;
        }
        return res;
    }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares obj = new DetectSquares();
 * obj.add(point);
 * int param_2 = obj.count(point);
 */

