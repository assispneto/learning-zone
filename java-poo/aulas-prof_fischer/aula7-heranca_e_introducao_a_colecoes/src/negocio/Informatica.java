package negocio;

public class Informatica extends Produto {

	public Informatica(int id, String nome) {
		super(id, nome);

	}

	public void teste() {

		this.nome = "fa";
	}

	public String imprimir() {

		return " Filho -  id: " + this.id + " nome: " + this.nome;
	}

}
