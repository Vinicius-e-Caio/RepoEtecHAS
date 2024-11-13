using CommunityToolkit.Mvvm.ComponentModel;
using MeteorologyPrevision.Models;
using MeteorologyPrevision.Services;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MeteorologyPrevision.ViewModel
{
    public partial class MeteorologyViewModel : ObservableObject
    {
        [ObservableProperty]
        ObservableCollection<Metereology> meteoreologies;

        public MeteorologyViewModel()
        {
            Meteoreologies = new ObservableCollection<Metereology>();
        }

        public async Task getClimates(string name)
        {
            MeteorologyService meteorologyService = new MeteorologyService();
            Meteoreologies = await meteorologyService.getClimate(name);
        }
    }
}
