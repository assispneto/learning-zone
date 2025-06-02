// Questao 2
// Verifique se A eh menor que 10, se verdade imprima: "A < 10", e verifique
// se o A mais B eh igual a 20, se verdade imprima: "A + B == 20". Caso
// nenhumas das afirmação nao seja verdadeira, imprima: "numero nao
// valido", (obs: apenas uma impressão é permitida na saída do programa).

package lista1_estruturas_de_decisao;
import java.util.Scanner;

public class Questao02 {
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
		
		if (a<10) {
			System.out.print("# A<10");
		} else if (a+b == 20){
			System.out.print("A+B = 20");
		} else {
			System.out.print("Número não válido!");
		}
	}
}


