import java.util.concurrent.Semaphore;

class H2O {
    private Semaphore H = new Semaphore(2);
    private Semaphore O = new Semaphore(0);
    public H2O() {
        
    }

    public synchronized void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
		H.acquire();
        // releaseHydrogen.run() outputs "H". Do not change or remove this line.
        releaseHydrogen.run();
        if (H.availablePermits() == 0) {
            O.release();
        }
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        O.acquire();
        // releaseOxygen.run() outputs "O". Do not change or remove this line.
		releaseOxygen.run();
        H.release(2);
    }
}

