class Solution {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses, (c1, c2) -> c1[1] - c2[1]);
        PriorityQueue<Integer> taken = new PriorityQueue<>((d1, d2) -> d2 - d1);
        int time = 0;
        for (int[] course : courses) {
            if (course[0] > course[1]) {
                System.out.println("continue");
                continue;
            }
            if (course[0] + time <= course[1]) {
                time += course[0];
                taken.add(course[0]);
            } else if (!taken.isEmpty() && taken.peek() > course[0]) {
                time += course[0] - taken.poll();
                taken.add(course[0]);
            }
        }
        return taken.size();
    }
}

