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
    public class MeteorologyService
    {
        private HttpClient httpClient;
        private ObservableCollection<Metereology> items;
        private JsonSerializerOptions jsonSerializerOptions;
        private string ApiKey = "0bac2f5673a12005123bbb73509f9b7e";

        public MeteorologyService()
        {
            items = new ObservableCollection<Metereology>();
            httpClient = new HttpClient();
            jsonSerializerOptions = new JsonSerializerOptions
            {
                PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
                PropertyNameCaseInsensitive = true,
                WriteIndented = true
            };
        }
        public async Task<ObservableCollection<Metereology>> getClimate(string name)
        {
            Uri uri = new Uri($"https://api.openweathermap.org/data/2.5/weather?lat=-23.36&lon=-46.84&appid=0bac2f5673a12005123bbb73509f9b7e");

            
            try
            {
                HttpResponseMessage response = await httpClient.GetAsync(uri);
                if (response.IsSuccessStatusCode)
                {

                    var content = await response.Content.ReadAsStringAsync();
                    var itemsModel = JsonSerializer.Deserialize<Metereology>(content, jsonSerializerOptions);
                    if (itemsModel != null)
                    {
                        items.Clear();
                        items.Add(itemsModel);
                    }

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
