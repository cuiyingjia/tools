import java.util.*;

public class DefiniteIntegralApp {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

            //define the upper limit and the lower limit
            double a = 2;
            double b = 5;

            double sum = 0;
            //get the gap, the smaller gap ,the smaller margin of error
            double e = gap(a, b, 10000.0);

            //sum the portion, from 1 to n
            for (int j = 1; j <= 10000; j++) {
                double x = median(a, b, 10000.0, j);
                sum = sum + f(x);

            }
            System.out.print("f(x)=2*x*x+x的定积分：");
            System.out.println(sum * e);

        }

    // define the integral fucntion 
    public static double f(double x) {
        //for example: f(x)=2*x*x+x
        return 2*x*x+x;
    }

    //define the median of the portion number i, which means define integral variable
    public static double median(double a, double b, double n, int i) {
        return a + i * (b - a) / n;
    }

    // define each gap of the portion, which means divided the range into portion N
    public static double gap(double a, double b, double n) {
        return (b - a) / n;
    }
}




