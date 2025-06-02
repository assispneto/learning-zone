package OO;

public class Teste {

	public static void main(String[] args) {
		
		int             a               = 20;
		ControleRemoto  controleRemoto  = new ControleRemoto();

		ControleRemoto  tv  = new ControleRemoto();

		controleRemoto.numeroCanal=20;
		tv.numeroCanal =500;
		
		System.out.println(controleRemoto.numeroCanal);
		System.out.println(tv.numeroCanal);
		tv.avancarCanal();
		System.out.println(tv.numeroCanal);
		tv.voltarCanal();
		System.out.println(tv.numeroCanal);
		
		tv.escolherCanal(30);
		System.out.println(tv.numeroCanal);
		
		
	}

}
