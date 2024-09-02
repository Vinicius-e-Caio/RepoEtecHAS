public class CriarLivro {
    public static void main(String[] args) {
        Editora primeiraEditora = new Editora();
        primeiraEditora.nome = "deJesusEdith";
        primeiraEditora.site = "www.deJesus.com.br";
        //System.out.println(primeiraEditora.nome + " do site " + primeiraEditora.site + " é minha editora favorita!");

        Editora segundaEditora = new Editora();
        segundaEditora.nome = "GlobiGlobi";
        segundaEditora.site = "www.GlobiGlobi.com.xx";

        Autor autor1 = new Autor();
        autor1.nome = "Vinicius di Jeskespare";
        autor1.telefone = "11-977831859";
        autor1.email = "viniciusfilho09@gmail.com";
        autor1.foto = "fotinhaParaOGP.raw";

        Livro favorito = new Livro();
        favorito.titulo = "Maze Runner";
        favorito.autor = autor1;
        favorito.preco = 100.00;
        favorito.paginas = 254;
        favorito.editora = primeiraEditora;
        favorito.tipoCapa = TipoCapaEnum.COMUM;
        /* System.out.println(favorito.titulo + " do autor " +
                favorito.autor.nome +
                " do número " +
                autor1.telefone +
                " é meu livro favorito!" +
                " é distribuído pela editora " +
                favorito.editora.nome);*/
        favorito.exibirDadosdoLivro();
        System.out.println("O Desconto é: " + favorito.calcularDesconto(10.00));
    }
}
