using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MauiAppTest.Models
{
    public class Dice
    {
        public int NumeroDeLados { get; set; }
        public int NumeroSorteado { get; set; }
 
        public void Rolar()
        {
            NumeroSorteado = new Random().Next(NumeroDeLados) + 1;
        }

        public Dice(int numeroDeLados)
        {
            NumeroDeLados = NumeroDeLados;
        }
    }
}
