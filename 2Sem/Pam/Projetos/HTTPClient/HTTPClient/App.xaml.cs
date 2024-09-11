using HTTPClient.Views;

namespace HTTPClient
{
    public partial class App : Application
    {
        public App()
        {
            InitializeComponent();

            MainPage = new PostView();
        }
    }
}
