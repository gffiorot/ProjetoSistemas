import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int primeiro, segundo;
        Scanner sc = new Scanner(System.in);

        String msg = "*********************\n" +
                "Escolha uma opção:\n" +
                "1) Soma\n" +
                "2) Subtração\n" +
                "3) Multiplicação\n" +
                "4) Divisão\n" +
                "0) Sair\n";

        try{
            System.out.print(msg);
            int opcao = sc.nextInt();

            if (opcao == 0) {
                System.out.println("*********************");
            }
            else if (opcao >= 1 && opcao <= 4) {
                System.out.println("Digite o primeiro inteiro:");
                primeiro = sc.nextInt();
                System.out.println("Digite o segundo inteiro:");
                segundo = sc.nextInt();

                switch (opcao) {
                    case 1:
                        System.out.println("A resposta é : "+(primeiro + segundo));
                        break;
                    case 2:
                        System.out.println("A resposta é : "+(primeiro - segundo));
                        break;
                    case 3:
                        System.out.println("A resposta é : "+(primeiro * segundo));
                        break;
                    case 4:
                        try {
                            System.out.println("A resposta é : "+(primeiro / segundo));
                        } catch (ArithmeticException e) {
                            System.out.println("Não pode dividir por zero.");
                        }
                        break;
                }
            }
            else {System.out.println("Opção invalida");}

        } catch (InputMismatchException e) {
            System.out.println("Apenas números inteiros aceitos");
        }
    sc.close();
    }
}
