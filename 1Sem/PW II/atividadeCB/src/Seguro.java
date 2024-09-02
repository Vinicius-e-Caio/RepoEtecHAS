public class Seguro {
    public double valor;
    public Pessoa pessoa;
    public double CalcularSeguro(){
        if (this.pessoa.sexo.equals('F'))
            return this.valor * 0.10;
        else
            return this.valor*0.20;
    }
}
