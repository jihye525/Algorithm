import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n1 = scanner.nextInt();
        int n2 = scanner.nextInt();
        int n3 = scanner.nextInt();
        int reward = 0;
        if (n1 != n2 && n1 != n3 && n2 != n3){
           reward = Math.max(Math.max(n1,n2), Math.max(n2, n3)) * 100;
        }else{
            if(n1 == n2 || n1 == n3){
                reward = 1000 + n1 * 100;
                if(n2 == n3){
                     reward = 10000 + n1 * 1000;
                }
            }else{
                reward = 1000 + n2 * 100;
           }
        }
       System.out.println(reward); 
    }
}