
public class Conta {

	// atributos - qualidade -estado

	public int numero;
	public int codigo;
	public double valor;

    public Banco banco;
	
	
	// construtor
	public Conta(int numero, int codigo) {
		this.numero = numero;
		this.codigo = codigo;

	}

	public Conta(int codigo) {
		this.codigo = codigo;

	}

	public void teste() {
		System.out.println("Olá sou um teste");
	}

	// metodos - verbos
	public double sacar(double valor) {
		System.out.println("valor dentro do metodo" + valor);
		if (valor <= 0)
			return 0;
		else
			this.valor -= valor;
		System.out.println("valor dentro do metodo fim " + valor);

		return valor;
	}
}
