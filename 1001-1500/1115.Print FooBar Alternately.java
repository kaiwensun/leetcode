class FooBar {
    private int n;
    private boolean fooStarted = false;

    public FooBar(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        print(printFoo);
    }

    public void bar(Runnable printBar) throws InterruptedException {
        synchronized(this) {
            if (!fooStarted && n > 0) {
                this.wait();
            }
        }
        print(printBar);
    }

    private void print(Runnable runnable) throws InterruptedException {
        for (int i = 0; i < n; i++) {
        	synchronized(this) {
                runnable.run();
                fooStarted = true;
                this.notify();
                if (i != n - 1) {
                    this.wait();
                }
            }
        }
    }
}

