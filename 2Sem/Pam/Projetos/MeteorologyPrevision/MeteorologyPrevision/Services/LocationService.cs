using MeteorologyPrevision.Models;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace MeteorologyPrevision.Services
{
    public class LocationService
    {
        private HttpClient httpClient;
        private JsonSerializerOptions jsonSerializerOptions;

        public LocationService()
        {
            httpClient = new HttpClient();
            jsonSerializerOptions = new JsonSerializerOptions { 
                PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
                WriteIndented = true
            };
        }
        public async Task<ObservableCollection<Location>> getLocations()
        {
            Uri uri = new Uri("https://brasilapi.com.br/api/cptec/v1/clima/previsao/" );
            //TO DO: variável para linkar a view com ViewModel
            ObservableCollection<Meteorology> items = new ObservableCollection<Meteorology>();

            try
            {
                HttpResponseMessage response = await httpClient.GetAsync(uri);
                if (response.IsSuccessStatusCode)
                {
                    string content = await response.Content.ReadAsStringAsync();
                    items = JsonSerializer.Deserialize<ObservableCollection<Meteorology>>(content, jsonSerializerOptions);
                }
            }
            catch (Exception ex)
            {
                Debug.WriteLine(ex.Message);
            }
            return items;
        }
    }
}
