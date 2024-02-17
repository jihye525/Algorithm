import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int total = scanner.nextInt();
        int count = scanner.nextInt();
        int hap = 0;
        
        for(int i = 0; i<count; i++){
            int price = scanner.nextInt();
            int num = scanner.nextInt();
            hap += price * num;
        }
        
        if(hap == total){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
    }
}
    