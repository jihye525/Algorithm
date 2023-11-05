import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int mymax = Integer.MIN_VALUE;
        int mymin = Integer.MAX_VALUE;
         while(num--> 0) {
            int temp = sc.nextInt();
            mymax = mymax < temp ? temp : mymax;
            mymin = mymin > temp ? temp : mymin; 
        }
        System.out.println(mymax*mymin);
        
    }
}