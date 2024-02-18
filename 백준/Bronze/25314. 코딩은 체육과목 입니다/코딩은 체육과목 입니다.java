import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        String name = "int";
        for(int i = 0; i < N; i+=4){
            name = "long " + name;
        }
        
        System.out.println(name);
        
    }
}