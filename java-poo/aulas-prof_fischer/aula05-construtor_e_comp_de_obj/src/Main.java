
public class Main {

	public static void main(String[] args) {

		// objeto conta 
		Conta picPay = new Conta(10,3);
        Aluno joao= new Aluno(2020, "3030", "joao");
        joao.conta = picPay;
        joao.conta.banco= new Banco("Bradesco");

        Aluno maria = new Aluno(30, "6060", "maria");
        Conta nubank = new Conta(40, 50);
        nubank.banco= new Banco("nuBank");
        maria.conta= nubank;
        
  
        Apresentacao ap = new Apresentacao();
        System.out.println(ap.print(joao));
        
        System.out.println(ap.print(maria));
        
        
        
        
//        conta.numero= 50;
//        conta.codigo= 30;
//        
//        
//        System.out.println("numero: "+ conta.numero);
//        System.out.println("codigo: "+ conta.codigo);
//        
//		
//		conta.valor = 1000;
//		System.out.println(conta.valor);
//		conta.sacar(100);
//		System.out.println(conta.valor);
//		

	}
}
