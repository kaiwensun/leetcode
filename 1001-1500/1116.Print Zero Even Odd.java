import java.util.concurrent.Semaphore;

class ZeroEvenOdd {
    private int n;
    private Semaphore zeroSem;
    private Semaphore oddSem;
    private Semaphore evenSem;
    
    public ZeroEvenOdd(int n) {
        this.n = n;
        this.zeroSem = new Semaphore(1);
        this.oddSem = new Semaphore(0);
        this.evenSem = new Semaphore(0);
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i ++) {
            zeroSem.acquire();
            printNumber.accept(0);
            Semaphore nextSem = i % 2 == 1 ? oddSem : evenSem;
            nextSem.release();
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for (int i = 2; i <= n; i += 2) {
            evenSem.acquire();
            printNumber.accept(i);
            zeroSem.release();
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i += 2) {
            oddSem.acquire();
            printNumber.accept(i);
            zeroSem.release();
        }
    }
}

