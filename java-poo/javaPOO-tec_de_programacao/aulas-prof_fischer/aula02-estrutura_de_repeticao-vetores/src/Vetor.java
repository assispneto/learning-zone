import java.util.Scanner;

public class Vetor {

	public static void main(String[] args) {

		Scanner entrada = new Scanner(System.in);

		int a = 20;
		int vet[] = new int[4];

		int cont = 0;
		while (cont <= 3) {

			System.out.println("Por favor, digite um valor: ");
//			System.out.println(entrada.nextInt());
			vet[cont]=entrada.nextInt();
			cont++;
		}

	
		for (int i = 0; i < vet.length; i++) {
			System.out.println("morador " + (i + 1) + "  " + vet[i] );
		}

		System.out.println();
	}
}
