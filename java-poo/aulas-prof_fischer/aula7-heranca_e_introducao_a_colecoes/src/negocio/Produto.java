package negocio;

public abstract class Produto {

	protected   int id;
	protected  String nome;
	
	// relacionamento de "ter"
	private Valor valor;
	
	
	public Produto (int id, String nome) {
		
		// relacionamento de usar
		ValidadorDados validar = new ValidadorDados();
		
		if(validar.validarDados(id))
			 this.id= id;
		
		this.nome= nome;
	}
	
	public Produto (ValidadorDados validar) {
		
	}
	
	public String imprimir() {
		
		return " Pai -  id: "+ this.id + " nome: " + this.nome;
	}
}
