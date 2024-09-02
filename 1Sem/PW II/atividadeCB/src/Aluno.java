public class Aluno {
    int id;
    String nome;
    String celular;
    String cpf;
    Curso idCurso;

    public String exibirDados() {
        return "O Aluno " + this.nome + " do código " + this.id + ", faz o curso " + this.idCurso.nome;
    }
}
