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
        ObservableCollection<Meteorology> meteorologies;

        public MeteorologyViewModel()
        {
            Meteorologies = new ObservableCollection<Meteorology>();
        }

        public async Task getClimates(int id)
        {
            MeteorologyService meteorologyService = new MeteorologyService();
            Meteorologies = await meteorologyService.getClimate(id);
        }
    }
}
