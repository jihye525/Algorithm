import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner key = new Scanner(System.in);
        int n1 = key.nextInt();
        int n2 = key.nextInt();
        int factor = 0;
        
        System.out.println(n1 * (n2 % 10));
        System.out.println(n1 * (n2 % 100 / 10));
        System.out.println(n1 * (n2 / 100));
        System.out.println(n1 * n2);
        
    }
}