package negocio;

public class Main {

	public static void main(String[] args) {

		Fruteira fruteira = new Fruteira(20, "banana");
		// System.out.println(p.imprimir());

		Informatica informatica = new Informatica(50, "pendrive");
		// System.out.println(p1.imprimir());

		Produto padaria = new Padaria(30, "pao");
		// System.out.println(p1.imprimir());

		// CarrinhoCompras carrinho = new CarrinhoCompras();
		//
		// Mecanica m = new Mecanica(45, "troca de oleo");
		//
		// carrinho.addProduto(fruteira);
		// carrinho.addProduto(informatica);
		// carrinho.addProduto(padaria);
		// carrinho.addProduto(m);
		//
		// carrinho.imprimirProdutos();

		CarrinhoCompraMelhorado carrinho = new CarrinhoCompraMelhorado();

		Mecanica m = new Mecanica(45, "troca de oleo");

		for (int i = 0; i < 100; i++) {
			carrinho.addProduto(fruteira);
			carrinho.addProduto(informatica);
			carrinho.addProduto(padaria);

		}

		carrinho.imprimirProdutos();

	}

}
