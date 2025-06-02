package lista2;
import java.util.Arrays;
import java.util.Collections;

public class Utilidades {
	
	// Questao 1
	public static int somar(int vetor[]){
		int soma = 0;
		for (int i=2; i<(vetor.length)-2; i++) {
			soma = vetor[i]+soma;
		}
		return soma;
	}
	
	// Questao 2
	public static int[] numPares(int inicio, int fim){
		// Para definir o tamanho do meu vetor, primeiro irei
		// descobrir a quantidade de numeros pares presentes
		// na sequencia 
		int quantidadePar = 0;
		for (int i=inicio; i<fim; i++) {
			if (i%2 == 0) {
				quantidadePar++;
			}
		}
		// Crio meu vetor com base no tamanho encontrado
		int vetorPar[] = new int[quantidadePar];
		int cont = 0;
		for (int i=inicio; i<fim; i++) {
			if (i%2 == 0) {
				vetorPar[cont] = i;
			}
			cont++;
		}
		return vetorPar;
	}
	
	// Questao 3
	public static int media(int vetorA[], int vetorB[]){
		int somaVetores = 0;
		int tamanho 	= vetorA.length;
		int media		= 0;
		for (int i=0; i<vetorB.length; i++) {
			somaVetores = (vetorA[i]+vetorB[i]) + somaVetores;
		}
		media = (somaVetores/tamanho);
		return media;
	}
	
	// Questao 4
	public static float mediaPonderada(int vetorNota[], int vetorPeso[]){
		int 	denominador 	= 0;
		int		ponderado		= 0;
		float	mediaPonderada	= 0;
		for (int i=0; i<vetorPeso.length; i++) {
			ponderado	= (vetorNota[i]*vetorPeso[i]) + (vetorNota[i+1]*vetorPeso[i+1]);
			denominador = vetorPeso[i]+denominador;
		}
		mediaPonderada = (ponderado/denominador);
		return mediaPonderada;
	}
	
	// Questao 5
	public static int contaElementos(int vetor1[], int vetor2[], int valorContado) {
		int count = 0;
		// Contando no vetor 1
		for (int i=0; i<vetor1.length; i++) {
			if (vetor1[i] == valorContado) {
				count++;
			}		
		}
		for (int i=0; i<vetor2.length; i++) {
			if (vetor2[i] == valorContado) {
				count++;
			}		
		}
		return count;
	}
	
	// Questao 6
	public static int[] copiaVetor(int vetor[]) {
		int vetorCopiado[] = new int[vetor.length];
		for (int i=0; i<vetorCopiado.length; i++) {
			vetorCopiado[i] = vetor[i];
		}
		return vetorCopiado;
	}
	
	// Questao 7
	public static int ordenar(int vetor[]) {
		int aux = 0;
		for (int i=0; i<vetor.length; i++) {
			for (int j=0; j<vetor.length; j++) {
				if(vetor[i] < vetor[j]) {
					aux = vetor[i];
					vetor[i] = vetor[j];
					vetor[j] = aux;
				}
			}
		}
		
		
		
	// Questao 8
	
	
	// Questao 9
	
	
	// Questao 10
	
	
	// Questao 11
	public static boolean verificaIgualdade(int vetor1[], int vetor2[]) {
		boolean verificacao = false;
		for (int i=0; i<vetor2.length; i++) {
			if(vetor1[i] == vetor2[i]) {
				verificacao = true;
			} else {
				return verificacao = false;
			}
		}
		return verificacao;
	}
	
	
	
	
	
	
	
	
	
}
