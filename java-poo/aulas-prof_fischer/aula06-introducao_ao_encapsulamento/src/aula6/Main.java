package aula6;

public class Main {

	public static void main(String[] args) {

		Produto produto1 = new Produto("Pendrive", 10);
		Produto produto2 = new Produto("Impressora", 20);
		Produto produto3 = new Produto("Caderno", 30);

		// produto1.print();
		// produto2.print();
		// produto3.print();

		int vet[] = new int[10];

		Produto produtos[] = new Produto[3];

		produtos[0] = produto1;
		produtos[1] = produto2;
		produtos[2] = produto3;
		//
		// for (int i = 0; i < produtos.length; i++) {
		// produtos[i].print();
		// }
		//
		// for (Produto produto : produtos) {
		// produto.print();
		// }
		//
		Produto aux = null;

		Produto lista[] = new Produto[1000];

		for (int i = 0; i < 1000; i++) {
			aux = new Produto();
			// aux.codigo =i;
			// aux.nome = "p_" + i;
			aux.setValor((i * 30) / 40);
			if (i % 2 == 0) {
				aux.setValor(aux.getValor() * -1);
			}

			lista[i] = aux;
		}

		// lista[1].nome="Caderno da Raissa";
		// lista[1].codigo= 50;

		// for (int i = 0; i < lista.length; i++) {
		// lista[i].print();
		// }
		

		for (Produto p : lista) {
			p.print();
			System.out.println(p.getValor());
		}

	}

}
