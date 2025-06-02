
public class ExemploPrimeiraClasse {

	public static void main(String[] args) {

		// // comentarios
		/*
		 * comentarios 
		 * de 
		 * mais 
		 * de 
		 * uma 
		 * linha
		 */

		// impressao de mensagem
		System.out.print("Ola Mundo!" + " tecnicas \n");

		// variaveis
		int numero1 = 0;
		numero1 = 20;
		System.out.println(numero1);

		int numero2 = 20;
		char letra;
		float decimal = 1.3f;
		double decimalDouble = 2.3d;
		String nome = "joao";
		boolean verdade = false;

		// concatenacao
		System.out.println("nome da pessoa: " + nome + " - " + verdade + " " + numero1 + numero2);
		//

		// operadores logicos
		boolean x = true;
		boolean y = false;

		// and
		System.out.println(x && y);

		// or
		System.out.println(x || y);

		// negacao
		System.out.println(!x);

		int a = 10;
		int b = 0;

		// incrementos
		b = a++; // a = a + 1
		b = a--; // a= a-1

		// operacoes de decisao

		boolean teste = false;
		int numero = 4;

		if (numero != 20)
			System.out.println("entrou dentro do if");
		else
			System.out.println("entrou dentro do else");

		// ifs anilhados
		if (numero >= 20)
			System.out.println("numero maior que 20");
		else if (numero >= 10)
			System.out.println("numero menor que 10");
		else if (numero >= 15)
			System.out.println("numero 15");
		else
			System.out.println("else");

		// if interno
		if (numero % 2 == 0) {
			System.out.println("par");

			if (numero == 10)
				System.out.println(" numero igual 10");
		} else
			System.out.println("impar");

		// if e else interno
		int num = 10;
		if (num > 10) {
			if (num > 20) {
				System.out.println("numero aceito");
			} else {
				System.out.println("numero nao aceito");
			}
		} else {
			System.out.println("numero menor que 10");
		}

		// if com expressao logica
		if (num > 10 && num > 20) {
			System.out.println("numero aceito");
		} else {
			System.out.println("numero nao aceito");
		}

		// estrutura de decisao switch

		int numeroTeste = 0;
		numeroTeste = 10;
		switch (numeroTeste) {

		case 10:
			System.out.println("numero 10");
			break;

		case 20:
			System.out.println("numero 20");
			break;

		case 25:
			System.out.println("numero 25");
			break;

		default:
			break;
		}
	}
}
