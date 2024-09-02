using CommunityToolkit.Mvvm.ComponentModel;
using FaceCoin.Models;
using FaceCoin.Views;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace FaceCoin.ViewModel
{
    public partial class FlipViewModel : ObservableObject
    {
        [ObservableProperty]
        public string _pickerChoice;

        [ObservableProperty]
        public string _imgCoin;

        [ObservableProperty]
        public string _resultLabel;

        public ICommand FlipCommand {  get; private set; }

        public FlipViewModel()
        {
            FlipCommand = new Command(Flip);
            ImgCoin = $"coroa.png";
        }

        public void Flip() 
        {
            Flip flip = new Flip();
            ResultLabel = flip.Rolar(PickerChoice);
            ImgCoin = $"{flip.lado}.png";
        }


    }
}
