using System;

namespace MauiAppTest
{
    public partial class MainPage : ContentPage
    {
        int numeroAleatorio = 0;

        public MainPage()
        {
            InitializeComponent();
            SidesNumberPicker.SelectedIndex = 0;
        }

        private void RollDiceButton_Clicked(object sender, EventArgs e)
        {
            //Pegar o número selecionado pelo usuário
            int max = Convert.ToInt32(SidesNumberPicker.SelectedItem);
            //Sorteat um número que seja entre 1 e o número selecionado
            numeroAleatorio = new Random().Next(1, max + 1);
            //Exibir ele na label da interface
            DiceResultLabel.Text = numeroAleatorio.ToString();

        }
    }

}
