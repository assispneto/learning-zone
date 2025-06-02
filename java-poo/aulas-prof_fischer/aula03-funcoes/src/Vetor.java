import java.util.Scanner;

public class Vetor {

	public static void main(String[] args) {

		int a = 10;
		// int vet[] = {0,1,2,3};

		int vetA[] = new int[3];
		int vetB[] = new int[3];
		vetA[0] = 20;
		vetA[1] = 3;

		vetB[0] = 20;
		vetB[1] = vetA[1];

		
		Scanner entrada = new Scanner(System.in);
		
//		for (int i = 0; i < vetA.length; i++) {
//			vetA[i] = entrada.nextInt(); 
//		}
//		
//		for (int i = 0; i < vetA.length; i++) {
//			System.out.print(vetA[i] + " - "); 
//		}
		
		int vet[][]= new int[2][4];
		
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < 4; j++) {
				vet[i][j] = i+j; 
			}
		}
		
		
	}

}
