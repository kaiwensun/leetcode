class Foo {
    private int next = 1;

    private synchronized void attempt(Runnable runnable, int targetState) throws InterruptedException {
        while (next != targetState) {
            this.wait();
        }
        runnable.run();
        next += 1;
        this.notifyAll();
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

