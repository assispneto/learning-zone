// Questao 20
// Verifique se o valor de A é maior que 10 ou se a soma de A e B é igual
// a 20. Se pelo menos uma dessas afirmações for verdadeira, imprima
// "números válidos". Caso contrário, imprima "número não válido". Em
// qualquer caso, imprima "Sejam bem-vindos à disciplina de Técnicas de
// Programação"

package lista1_estruturas_de_decisao;
import java.util.Scanner;

public class Questao20 {
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
		
		boolean verificacao;
		
		if ( (a>10) || (a+b==20) ) {
			System.out.println("# Numeros validos");
			verificacao = true;
		} else {
			System.out.println("# Numeros nao validos");
			verificacao = false;
		}
		
		if (verificacao) {
			System.out.println("# Sejam bem-vindos à disciplina \r\n"
					+ "de Técnicas de Programação");
		} else {
			System.out.println("# Sejam bem-vindos à disciplina \r\n"
					+ "de Técnicas de Programação");
		}
	}
}


