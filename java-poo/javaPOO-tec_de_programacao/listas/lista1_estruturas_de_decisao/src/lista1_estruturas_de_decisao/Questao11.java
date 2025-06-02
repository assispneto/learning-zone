// Questao 11
// Verifique se A é maior que 10 se não for verifique se A mais B é igual a
// 20, imprima: "A + B == 20''. Caso A não seja maior que 10 e A mais B
// for diferente de 20, imprima: "número não válido"

package lista1_estruturas_de_decisao;
import java.util.Scanner;

public class Questao11 {
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
		
		if (a>10) {
			System.out.println("# A>10");
		} else if (a+b==20) {
			System.out.println("# A+B = 20");
		}
		
		if ( (a<10) && (a+b!=20) ) {
			System.out.println("# Numero nao valido");
		}
	}
}


