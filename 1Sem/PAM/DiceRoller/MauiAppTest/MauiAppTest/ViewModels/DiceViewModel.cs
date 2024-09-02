using CommunityToolkit.Mvvm.ComponentModel;
using MauiAppTest.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace MauiAppTest.ViewModels
{
    public partial class DiceViewModel : ObservableObject
    {
        [ObservableProperty]
        private int _numeroSorteado;

        [ObservableProperty]
        private int _numeroDeLados;

        public ICommand rollCommand { get;  }

        public void roll()
        {
            Dice dice = new Dice(_numeroDeLados);
            dice.Rolar();
            NumeroSorteado = dice.NumeroSorteado;
        }

        public DiceViewModel()
        {
            rollCommand = new Command(roll);
        }
    }
}
