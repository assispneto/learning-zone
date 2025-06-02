package aula6;

public class CarrinhoCompra {

	public String nome;
	public Produto[] lista;

	public CarrinhoCompra(int tamanho) {
		lista = new Produto[tamanho];
	}
	
	public  void popularLista() {
		for (int i = 0; i < lista.length; i++) {
			lista[i] = new Produto();
		}
	}
	
	public void imprimirProduto() {
		for (Produto p : lista) {
			  p.print();
		}
	}
}
