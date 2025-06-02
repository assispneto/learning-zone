import java.util.Random;

public class Funcao {

	// iterativo
	public static int somar(int vet[]) {

		int soma = 0;
		for (int i = 0; i < vet.length; i++) {
			soma += vet[i];
		}
		return soma;
	}

	// recursiva
	public static int somar2(int vet[], int soma, int num) {

		if (num < 0) {
			return soma;
		}
		soma += vet[num];

		return somar2(vet, soma, num - 1);
	}

	public static void main(String[] args) {

		int vet[] = new int[100000];

		Random aleatorio = new Random();
		for (int i = 0; i < vet.length; i++) {
			vet[i] = aleatorio.nextInt();
		}

		System.out.println(somar(vet));

//		System.out.println(somar2(vet, 0, vet.length - 1));
	}
}
