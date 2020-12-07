class FizzBuzz {
    private int n;
    private int num = 1;
    Semaphore semFizz = new Semaphore(0);
    Semaphore semBuzz = new Semaphore(0);
    Semaphore semFizzBuzz = new Semaphore(0);
    Semaphore semNum = new Semaphore(1);

    public FizzBuzz(int n) {
        this.n = n;
        this.num = 1;
    }

    private void print(Runnable runnable) {
        runnable.run();
        num ++;
        if (num <= n) {
            if (num % 3 == 0 && num % 5 == 0) {
                semFizzBuzz.release();
            }
            if (num % 3 == 0) {
                semFizz.release();
            } else if (num % 5 == 0) {
                semBuzz.release();
            } else {
                semNum.release();
            }
        } else {
            for (Semaphore sem : new Semaphore[] {semFizzBuzz, semFizz, semBuzz, semNum}) {
                sem.release();
            }
        }
    }

    // printFizz.run() outputs "fizz".
    public void fizz(Runnable printFizz) throws InterruptedException {
        while (true) {
            semFizz.acquire();
            if (num > n) {
                break;
            }
            print(printFizz);
        }
    }

    // printBuzz.run() outputs "buzz".
    public void buzz(Runnable printBuzz) throws InterruptedException {
        while (true) {
            semBuzz.acquire();
            if (num > n) {
                break;
            }
            print(printBuzz);
        }
    }

    // printFizzBuzz.run() outputs "fizzbuzz".
    public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        while (true) {
            semFizzBuzz.acquire();
            if (num > n) {
                break;
            }
            print(printFizzBuzz);
        }
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void number(IntConsumer printNumber) throws InterruptedException {
        while (true) {
            semNum.acquire();
            if (num > n) {
                break;
            }
            print(() -> printNumber.accept(num));
        }
    }
}

