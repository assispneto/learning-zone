package OO;

public class ControleRemoto {

	//qualidades  -  atributos
	public int numeroCanal;
	
	//comportamentos - metodos
	
	public void avancarCanal() {
		 numeroCanal++;
	}
	public void voltarCanal() {
		numeroCanal--;
	}
	
	public void escolherCanal(int numero) {
		numeroCanal = numero;
	}
	
}
