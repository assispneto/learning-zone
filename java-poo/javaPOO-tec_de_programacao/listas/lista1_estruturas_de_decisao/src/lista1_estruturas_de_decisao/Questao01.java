// Questao 1
// Verifique se A é maior que 10, se verdade imprima: "A > 10" e verifique
// se o A mais B é igual a 20, se verdade imprima: "A + B == 20". Caso a
// segunda afirmacao nao seja verdadeira, imprima: "numero nao valido".

package lista1_estruturas_de_decisao;
import	java.util.Scanner;

public class Questao01 {
	public static void main(String[] args) {
		 // [1] Recebendo valores do usuario
		 Scanner valorA = new Scanner(System.in);
		 Scanner valorB = new Scanner(System.in);
		 int a = 0;
		 int b = 0;
		 
		 // [2] Mensagem para o usuario definir os valores
		 System.out.print("Digite o valor A > ");
		 a = valorA.nextInt();
		 System.out.print("Digite o valor B > ");
		 b = valorB.nextInt();
		 
		 // [3] Condicoes estabelecidas na questao
		 if (a>10) {
			System.out.println("\n# A>10");
		 }
		 if (a+b == 20) {
			 System.out.println("\n# A+B = 20");
		 } else {
			 System.out.println("\n# Número não válido!");
		 }
	}
}


