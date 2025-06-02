
public class Recurssividade {

	public static void f3(int num) {
		System.out.println("f3 " + num);
		f1(num - 1);
	}

	public static void f2(int num) {
		System.out.println("f2 " + num);
		f3(num - 1);
	}

	public static void f1(int num) {
		System.out.println("f1 " + num);
		
		//condicao de parada
		if(num < 0)
			return;
		
		f2(num - 1);
	}

	public static void main(String[] args) {
		System.out.println("inicio");
		f1(10000);
		
//		for (int i = 0; i < 10000000; i++) {
//			System.out.println(i);
//		}
		System.out.println("fim");
	}
}
