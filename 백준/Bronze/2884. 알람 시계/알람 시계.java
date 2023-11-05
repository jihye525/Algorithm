import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int H = scanner.nextInt();
        int M = scanner.nextInt();
         
        if(H == 0){
            if(0 <= M && M < 45){
                H = 23;
                M = 60 - (45 - M);
            }else{
                M = M - 45;
            }   
        }else{
            if(0 <= M && M < 45){
                H = H - 1;
                M = 60 - (45 - M);
            }else{
                M = M - 45;
            }   
        }
        System.out.println(H+" "+M);
    }
}