import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        int sum = 0;
        if(num % 2 == 0){
            for(int i = 0; i < num/2; i++){
                sum += num+1;
            }
        }else{
            for(int i = 0; i < num/2; i++){
                sum += num+1;
            }
            sum += num/2 + 1;
        }
        System.out.println(sum);
       
    }
}