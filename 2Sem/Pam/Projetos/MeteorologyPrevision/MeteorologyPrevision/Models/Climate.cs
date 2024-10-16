using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MeteorologyPrevision.Models
{
    public class Climate
    {
       public string Data { get; set; }
       public string Condicao { get; set;  }
       public string Condicao_desc { get; set;   }
       public int Min{ get; set; }
       public int Max { get; set; }
       public int Indice_uv { get; set;  }
    }
}
