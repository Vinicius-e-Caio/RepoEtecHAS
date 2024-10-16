using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MeteorologyPrevision.Models
{
    public class Meteorology
    {
        public string Cidade { get; set;  }
        public string Estado { get; set;  }
        public string Atualizado_em { get; set;  }
        public ObservableCollection<Climate> Clima { get; set; }
    }
}
