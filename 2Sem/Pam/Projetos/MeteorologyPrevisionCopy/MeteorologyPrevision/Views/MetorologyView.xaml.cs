using MeteorologyPrevision.ViewModel;
using Microsoft.Maui.Graphics.Text;


namespace MeteorologyPrevision.Views;

public partial class MetorologyView : ContentPage
{
	private MeteorologyViewModel viewModel;
	public MetorologyView()
	{
		InitializeComponent();
        viewModel = new MeteorologyViewModel();
		BindingContext = viewModel;
    }

   

    private async void LocationEntry_Completed(object sender, EventArgs e)
    {
		string LocationText = ((Entry)sender).Text;

		if (LocationText == null) {
			DisplayAlert("Erro", "Você deve digitar o id na caixa indicada", "Ok");
			return;
		}

		await viewModel.getClimates(LocationText);
    }
}