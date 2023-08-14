import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner key = new Scanner(System.in);
        int a = key.nextInt();
        int b = key.nextInt();
        int c = key.nextInt();

        System.out.println((a+b)%c);
        System.out.println(((a%c)+(b%c))%c);
        System.out.println((a*b)%c);
        System.out.println(((a%c)*(b%c))%c);

    }
}