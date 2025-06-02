package aula6;

public class Produto {

	private String nome;
	private int codigo;
	private double valor;

	// construtor
	public Produto(String nome, int codigo) {
		this.nome = nome;
		this.codigo = codigo;
	}

	public Produto() {
		// this.codigo=10;
		// this.nome="produto sem nome";
	}

	public String getNome() {
		return this.nome;
	}

	public void setValor(double valor) {
		if (valor > 0)
			this.valor = valor;
	}
	
	public double getValor() {
		return valor;
	}

	public void print() {
		System.out.println("nome: " + this.nome + " codigo: " + this.codigo);
	}

}
