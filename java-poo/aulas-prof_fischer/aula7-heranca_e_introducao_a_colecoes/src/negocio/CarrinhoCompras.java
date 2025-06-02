package negocio;

public class CarrinhoCompras {

	Produto produtos[] = new Produto[10];
	
	
	// metodo polimorfico
	public void addProduto(Produto p ){
		
		int indice = 0;
		for (int i = 0; i < produtos.length; i++) {
			
			if(produtos[i] == null) {
				indice = i;
			}
		}
		produtos[indice]= p;
	}
	
	public void imprimirProdutos() {
		System.out.println("itens comprados! ");
		
		for (int i = 0; i < produtos.length; i++) {		
			if(produtos[i]!= null )
              System.out.println(produtos[i].imprimir());
		}	
	}
}
