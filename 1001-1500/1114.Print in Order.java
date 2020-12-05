class Foo {
    private Integer next = 1;
    private Object lock = new Object();

    private void attempt(Runnable runnable, int targetState) throws InterruptedException {
        synchronized(lock) {
            while (next != targetState) {
                lock.wait();
            }
            runnable.run();
            next += 1;
            lock.notifyAll();
        }
    }

    public void first(Runnable printFirst) throws InterruptedException {
        attempt(printFirst, 1);
    }

    public void second(Runnable printSecond) throws InterruptedException {
        attempt(printSecond, 2);
    }

    public void third(Runnable printThird) throws InterruptedException {
        attempt(printThird, 3);
    }

}

