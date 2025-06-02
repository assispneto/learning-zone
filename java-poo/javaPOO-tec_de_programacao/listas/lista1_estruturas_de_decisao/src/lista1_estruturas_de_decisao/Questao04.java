// Questao 4
// Verifique se A eh maior que 10 ou se A mais B eh igual a 20, se verdade
// imprima: "numero valido". Caso as afirmacoes nao sejam verdadeiras,
// Verificar se A eh igual B, caso verdade imprima: (A eh igual B; A e B sao
// diferentes de 10; A eh menor que 10) caso nao seja verdade imprima:
// "numero nao valido"

package lista1_estruturas_de_decisao;
import java.util.Scanner;

public class Questao04 {
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
		
		if ( (a>10) || (a+b==20) ) {
			System.out.println("# Numero valido!");
		} else if (a==b) {
			System.out.println("# A eh igual a B; ");
			System.out.println("# A e B sao diferentes de 10; ");
			System.out.println("# A eh menor que 10.");
		} else {
			System.out.println("# Numero nao valido!");
		}
	}
}


