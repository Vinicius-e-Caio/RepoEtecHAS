using Microsoft.Maui.Graphics.Text;


namespace MeteorologyPrevision.Views;

public partial class MetorologyView : ContentPage
{
	public MetorologyView()
	{
		InitializeComponent();
		var LocalitionList = new List<string>();

	}

   

    private void LocationEntry_Completed(object sender, EventArgs e)
    {
		string LocationText = ((Entry)sender).Text;
		if (LocationText == null) {
			DisplayAlert("Erro", "Você deve digitar o id na caixa indicada", "Ok");
			return;
		}

		int LocationParsed = int.Parse(LocationText);
		

    }
}