import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int H = scanner.nextInt();
        int M = scanner.nextInt();
        int cook_minute = scanner.nextInt();
        
        if(M+cook_minute >= 60){
            H += (M+cook_minute) / 60;
            M = (M+cook_minute) % 60;
            if(H >= 24){
                H = H % 24;
            } 
        }else{
            M = M+cook_minute;
        }
        System.out.println(H+" "+M);
    }
}