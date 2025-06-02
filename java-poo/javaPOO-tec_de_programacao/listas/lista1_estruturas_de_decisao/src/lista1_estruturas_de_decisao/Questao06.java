// Questao 6
// Verifique se A é maior que 10, se verdade imprima: "A > 10" caso não
// seja, imprima: "A <= 10". Verifique se A mais B é igual a 20, se
// verdadeiro, imprima: "A + B == 20”, caso não seja imprima: “A + B !=
// 20”

package lista1_estruturas_de_decisao;

import java.util.Scanner;

public class Questao06 {
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
		
		// Condicao 1
		if (a>10) {
			System.out.println("# A>10");
		} else {
			System.out.println("# A<=10");
		}
		// Condicao 2
		if (a+b==20) {
			System.out.println("# A+B = 20");
		} else {
			System.out.println("# A+B != 20");
		}
	}
}


