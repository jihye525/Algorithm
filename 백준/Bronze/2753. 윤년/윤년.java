import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner key = new Scanner(System.in);
        int year = key.nextInt();
        
        if(year % 400 == 0){
            System.out.println(1);
        }else if(year % 100 == 0){
            System.out.println(0);
        }else if(year % 4 == 0){
            System.out.println(1);
        }else{
            System.out.println(0);
        }
    }
}