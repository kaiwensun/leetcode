class Cashier {

    private int n;
    private int discount;
    private Map<Integer, Integer> prices;
    private int counter;

    public Cashier(int n, int discount, int[] products, int[] prices) {
        this.n = n;
        this.discount = discount;
        this.prices = new HashMap<>();
        for (int i = 0; i < products.length; i++) {
            this.prices.put(products[i], prices[i]);
        }
        this.counter = 0;
    }
    
    public double getBill(int[] product, int[] amount) {
        counter ++;
        int total = 0;
        for (int i = 0; i < product.length; i++) {
            total += amount[i] * this.prices.get(product[i]);
        }
        return counter % n == 0 ? total * (double)(100 - discount) / 100 : (double)total;
    }
}

/**
 * Your Cashier object will be instantiated and called as such:
 * Cashier obj = new Cashier(n, discount, products, prices);
 * double param_1 = obj.getBill(product,amount);
 */
