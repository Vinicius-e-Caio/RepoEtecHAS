using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace FaceCoin.Models
{
    public class Flip
    {
        public string lado { get; set; }
     
        
        public string Rolar(string ladoEscolhido)
        {
            if (ladoEscolhido == null)
            {
                ladoEscolhido = "cara";
            }
            int ladoSorteado = new Random().Next(2);
            lado = ladoSorteado == 0 ? "cara" : "coroa";
            ladoEscolhido = ladoEscolhido.ToLower();
            string resultado = lado == ladoEscolhido ?
                $"Parabéns, você pediu {ladoEscolhido} e deu {lado}" :
                $"Meus sentimentos, você pediu {ladoEscolhido} e deu {lado}";
            return resultado;
        }


    }
}