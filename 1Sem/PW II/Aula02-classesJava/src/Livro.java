public class Livro {
    // Atributos
    String titulo;
    Autor autor;
    double preco;
    String resumo;
    int paginas;
    Editora editora;
    TipoCapaEnum tipoCapa;

    //Método construtor
    public Livro(String titulo){
        this.titulo = titulo;
    }
    public Livro(String titulo, double preco )
    //Métodos
    //public tipo_retorno momeMetodo([parametros]){}
    public void exibirDadosdoLivro(){
        String dadosLivro = "DETALHES DO LIVRO\n"
                + this.titulo
                + "\nAutor: " + this.autor.nome
                + "\nEditora: " + this.editora.nome
                + "\nTelefone: " + this.autor.telefone
                + "\n\nResumo: " + this.resumo
                + "\nPreço: " + this.preco;
        System.out.println(dadosLivro);
    }
    public Double calcularDesconto(Double percentualDeDesconto) {
        return this.preco * (percentualDeDesconto / 100);
    }
}


