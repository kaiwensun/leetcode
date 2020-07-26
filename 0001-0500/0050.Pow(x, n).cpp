class Solution {
public:
    double myPow(double x, int n) {
        if(x==1.0){
            return 1.0;
        }else if(x==-1.0){
            return n%2?-1.0:1.0;
        }else if(n==-2147483648){
            return myPowBaseNotOne(x,n+1)/x;
        }else{
            return myPowBaseNotOne(x,n);
        }
    }
private:
    double myPowBaseNotOne(double x, int n){
        if(n==0){
            return 1.0;
        }else if(n>0){
            double tmp = myPow(x,n/2);
            return n%2 ? tmp*tmp*x : tmp*tmp;
        }else{
            return 1/myPow(x, -n);
        }
    }
};
