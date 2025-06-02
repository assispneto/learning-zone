
public class Funcoes {

	// declarando
	public static int boasVindas() {
		System.out.println("ola seja bem vindo");
		System.out.println("Java");
		return 100;
	}

	public static int retornar10() {
		return 10;
	}

	public static int retornar20() {
		int numero = 20;
		return numero;
	}

	public static String cantar() {

		return "uauauauaua";
	}

	public static int somar(int valorA, int valorB) {

		return valorA + valorB;
	}

	public static void avidaComoVcVer() {
		cantar();
		cantar();
		somar(10, 20);
		somar(20, 30);
	}

	public static int[] retonarVetor() {

		System.out.println(" retornar vetor");
		int vet[] = new int[10];
		for (int i = 0; i < vet.length; i++) {
			vet[i] = i + 10;
		}
		return vet;
	}
	
	// //passagem eh por referencia (nao objeto)
	public static void  imprimirVetor(int vet[]) {
		vet[0]=45;
		for (int i = 0; i < vet.length; i++) {
			System.out.println(vet[i]);
		}
		
	}
	
	//passagem eh por valor (primitivos)
	public static void imprimir(int a) {
		a++;		
		System.out.println("a de dentro: "+ a);
	}
	
	public static int somarRetornar(int a, int vet[]) {
		
		int soma=a;
		for (int i = 0; i < vet.length; i++) {
			soma+= vet[i];
			vet[i]= soma + soma;
		}
				
		return soma;
	}
	

	public static void main(String[] args) {

		int vetorTeste[] = {5,10,25,12,405};
		
		System.out.println(somarRetornar(200, vetorTeste));
		
		for (int i = 0; i < vetorTeste.length; i++) {
			System.out.println(vetorTeste[i]);
		}
		
//		int a = 20;
//		System.out.println(a);
//		imprimir(a);
//		System.out.println(a);
//		
//		imprimirVetor(vetorTeste);
//		System.out.println();
//		 for (int i = 0; i < vetorTeste.length; i++) {
//				System.out.println(vetorTeste[i]);
//			}
//		 
//		// boolean verdade = (retornar10() + retornar20() == 30);
//		// System.out.println("soma: " + verdade);
//		//
//		// System.out.println(somar(10,20));
//		//
//		int vet[] = retonarVetor();
//		for (int i = 0; i < vet.length; i++) {
//			System.out.println(vet[i]);
//		}
//
////		for (int i = 0; i < retonarVetor().length; i++) {
////			System.out.println(retonarVetor()[i]);
////		}
//
//		// // chamando
//		// System.out.println(boasVindas());
//		//
//		// System.out.println(" 1");
//		//
//		// System.out.println(" 2 ");

		
		
		
		
		
		
	}
}
