
public class Apresentacao {


     public String print(Aluno  aluno) {
    	 String resposta="";
    	 
    	 resposta+="Aluno:  \n";
    	 resposta+= "Nome: "+ aluno.nome + " - ";
    	 resposta+= "CPF: " + aluno.cpf+ " - ";
    	 resposta+= "Matricula: " + aluno.matricula+ " - ";
    	 
    	 resposta+= "\n Conta: \n";
    	 resposta+= "Número: " +  aluno.conta.numero+ " - ";
    	 resposta+= "Valor: " +  aluno.conta.valor+ " - ";
    	 
    	 resposta+= "\nBanco: \n";
    	 resposta+="Nome:"+ aluno.conta.banco.nome;
    	 
    	 return resposta;
    	 
     }
}
