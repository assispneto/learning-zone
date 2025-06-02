package aula6;

public class Main2 {

	public static void main(String[] args) {

//		CarrinhoCompra c = new CarrinhoCompra(20);
//		c.popularLista();
//		c.imprimirProduto();

        Produto produto= new Produto("Pendrive", 10);
        produto.print();
//        produto.nome="Joao";
//        produto.codigo= 100;
        
        System.out.println(produto.getNome());
        produto.setValor(-20);
        System.out.println(produto.getValor());
//        produto.print();
        
	}

}
