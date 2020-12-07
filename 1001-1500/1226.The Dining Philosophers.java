class DiningPhilosophers {

    private final int PHI_NUM = 5;
    private boolean[] folks;

    public DiningPhilosophers() {
        folks = new boolean[PHI_NUM];
    }

    // call the run() method of any runnable to execute its code
    public synchronized void wantsToEat(int philosopher,
                           Runnable pickLeftFork,
                           Runnable pickRightFork,
                           Runnable eat,
                           Runnable putLeftFork,
                           Runnable putRightFork) throws InterruptedException {
        while (folks[philosopher] || folks[(philosopher + 1) % PHI_NUM]) {
            this.wait();
        }
        folks[philosopher] = true;
        folks[(philosopher + 1) % PHI_NUM] = true;
        pickLeftFork.run();
        pickRightFork.run();
        eat.run();
        putLeftFork.run();
        putRightFork.run();
        folks[philosopher] = false;
        folks[(philosopher + 1) % PHI_NUM] = false;
        this.notifyAll();
    }
}

