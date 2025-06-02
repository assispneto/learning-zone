// Questao 17
// Verifique se o valor de A é maior que 10 ou se a soma de A e B é igual
// a 20. Se pelo menos uma dessas afirmações for verdadeira, imprima
// "número válido". Caso contrário, verifique se A é igual a B. Se for
// verdade, imprima "A é igual B". Se A e B forem diferentes de 10 e A for
// menor que 10, imprima "A é menor que 10". Caso nenhuma das
// afirmações anteriores seja verdadeira, imprima "número não válido"

package lista1_estruturas_de_decisao;
import java.util.Scanner;

public class Questao17 {
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
		
		if( (a>10) || (a+b==20) ){
			System.out.println("# Numero valido! ");
		} else if (a==b) {
			System.out.println("# A eh igual a B");
		} else if ( (a!=10) && (b!=10) && (a<10) ) {
			System.out.println("# A eh menor que 10");
		} else {
			System.out.println("# Numero nao valido!");
		}
	}
}


