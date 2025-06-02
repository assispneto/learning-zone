// Questao 12
// Verifique se A é maior que 10 imprima: "A > 10" ou verifique se A mais
// B é igual a 20, imprima: "A + B == 20'', caso as afirmações não sejam
// verdadeiras, imprima: "números não válidos". Sejam as afirmações
// anteriores falsas ou verdadeiras imprima: “Sejam bem-vindos à
// disciplina de Técnicas de Programação”

package lista1_estruturas_de_decisao;
import java.util.Scanner;

public class Questao12 {
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
		
		/* OBS: como a questao deixa claro que 
		 * independente do retorno das afirmacoes, 
		 * a mensagem definida deve ser mostrada, 
		 * irei fazer uma verificao por mero capricho	 
		*/
		boolean verificacao; 
		
		if(a>10) {
			System.out.println("# A>10");
			if (a+b==20) {
				System.out.println("# A+B = 20");
				verificacao = true;
			}
			verificacao = true;
		} else {
			System.out.println("# Numeros nao validos");
			verificacao = false;
		}
		
		/* Atraves da seguinte estrutura, fica
		*  claro que independente do resultado,
		*  a mensagem sera mostrada 
		*/
		if (verificacao) {
			System.out.println("# Sejam bem-vindos a disciplina\r\n"
					+ "de Tecnicas de Programacao");
		} else {
			System.out.println("# Sejam bem-vindos a disciplina\r\n"
					+ "de Tecnicas de Programacao");
		}
	}
}



