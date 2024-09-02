using MauiAppTest.Models;
using MauiAppTest.ViewModels;

namespace MauiAppTest.Views;

public partial class NewPage1 : ContentPage
{
    int numeroAleatorio = 0;

    public NewPage1()
    {
        InitializeComponent();
        BindingContext = new DiceViewModel();
    }
}