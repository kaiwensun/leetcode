/**
 * 10 / 10 test cases passed.
 * Status: Accepted
 * Runtime: 34 ms
 * Your runtime beats 8.49% of java submissions.
 *Date:
 * 10/16/2016
 */

class NumArray {

    private ArrayList<ArrayList<Integer>> table = new ArrayList<>();
    public NumArray(int[] nums) {
        ArrayList<Integer> row = new ArrayList<>(nums.length);
        for(int n:nums)
            row.add(n);
        table.add(row);
        int r = 0;
        while(table.get(r).size()>1){
            row = new ArrayList<Integer>((table.get(r).size()+1)/2);
            for(int i=0;i<table.get(r).size()-1;i+=2){
                row.add(table.get(r).get(i)+table.get(r).get(i+1));
            }
            if(table.get(r).size()%2==1)
                row.add(table.get(r).get(table.get(r).size()-1));
            table.add(row);
            r++;
        }
    }

    public void update(int i, int val) {
        int inc = val-table.get(0).get(i);
        for(int r=0;r<table.size();r++){
            table.get(r).set(i,table.get(r).get(i)+inc);
            i = i>>1;
        }
    }

    public int sumRange(int i, int j) {
        return getPreSum(j+1)-getPreSum(i);
    }
    private int getPreSum(int i){
        if(table.size()==0 || i==0){
    		return 0;
    	}
    	if(table.size()==1){
    		return table.get(0).get(0);
    	}
        int sum = 0;
        int ind = 0;
        for(int r=table.size()-1;r>=0;r--){
            int step = 1<<r;
            if(i==step){
                sum+=table.get(r).get(ind);
                break;
            }
            if(i>=step/2){
                sum+=table.get(r-1).get(ind*2);
                ind = ind*2+1;
            }
            else{
                ind = ind*2;
            }
            i = i%(step/2);
            if(i==0)
                break;
        }
        return sum;
    }
}


// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.update(1, 10);
// numArray.sumRange(1, 2);
