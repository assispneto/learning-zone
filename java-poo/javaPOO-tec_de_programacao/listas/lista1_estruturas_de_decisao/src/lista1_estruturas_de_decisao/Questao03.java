// Questao 3
// Verifique se A eh igual a 10, se verdade imprima: "A == 10", e verifique
// se o A mais B eh igual a 20, se verdade imprima: "A + B == 20". verifique
// se o B eh igual a 10, se verdade imprima: "B == 10", (obs: todas as tres
// impressoes sao permitidas na saida do programa).

package lista1_estruturas_de_decisao;
import java.util.Scanner;

public class Questao03 {
	public static void main(String[] args) {
		Scanner valorA = new Scanner(System.in);
		Scanner valorB = new Scanner(System.in);
		int a = 0;
		int b = 0;
		 
		System.out.print("Digite o valor A > ");
		a = valorA.nextInt();
		System.out.print("Digite o valor B > ");
		b = valorB.nextInt();
		
		System.out.print("\n");
		
		if (a==10) {
			System.out.println("# A = 10");
		}
		
		if (b==10) {
			System.out.println("# B = 10");
		}
		
		if (a+b==20) {
			System.out.println("# A+B = 20");
		}
	}
}


