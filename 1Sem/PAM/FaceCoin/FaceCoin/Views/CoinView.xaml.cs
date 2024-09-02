using FaceCoin.ViewModel;

namespace FaceCoin.Views;

public partial class CoinView : ContentPage
{
	public CoinView()
	{
		InitializeComponent();

		BindingContext = new FlipViewModel();
	}

}