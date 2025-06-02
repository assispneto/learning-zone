// Questao7
// Verifique se A é maior que 10 ou se o A mais B é igual a 20, caso sejam
// verdadeiras as afirmações imprima: "números válidos”. Caso a primeira
// afirmação não seja verdadeira, imprima: "número não válido"

package lista1_estruturas_de_decisao;
import java.util.Scanner;

public class Questao07 {
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
		
		if( (a>10) || (a+b==20) ) {
			System.out.println("# Numeros validos");
			if (a<=10) {
				System.out.println("  -> Entretanto, o valor A nao eh valido");
			}
		}
	}
}


