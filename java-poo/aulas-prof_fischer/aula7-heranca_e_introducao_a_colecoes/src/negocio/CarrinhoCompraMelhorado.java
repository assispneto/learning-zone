package negocio;

import java.util.ArrayList;

public class CarrinhoCompraMelhorado {

	Produto produtos[] = new Produto[10];
    ArrayList <Produto> produtos_ = new ArrayList <Produto>();
	
	
	// metodo polimorfico
	public void addProduto(Produto p) {

		produtos_.add(p);
	}

	public void imprimirProdutos() {
		System.out.println("itens comprados! ");

		for (Produto produto : produtos_) {
			System.out.println(produto.imprimir());
		}
	}

}
