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
        private JsonSerializerOptions jsonSerializerOptions;

        public MeteorologyService()
        {
            httpClient = new HttpClient();
            jsonSerializerOptions = new JsonSerializerOptions
            {
                PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
                PropertyNameCaseInsensitive = true,
                WriteIndented = true
            };
        }
        public async Task<ObservableCollection<Meteorology>> getClimate(int id)
        {
            Uri uri = new Uri("https://brasilapi.com.br/api/cptec/v1/clima/previsao/"+id);
            
            try
            {
                HttpResponseMessage response = await httpClient.GetAsync(uri);
                if (response.IsSuccessStatusCode)
                {

                    string content = await response.Content.ReadAsStringAsync();
                    var meteorology = JsonSerializer.Deserialize<Meteorology>(content, jsonSerializerOptions);
                    if (meteorology != null)
                    {
                        var items = new ObservableCollection<Meteorology> { meteorology};
                        return items;
                    }                
                }
            }
            catch (Exception ex)
            {
                Debug.WriteLine(ex.Message);
            }
            return null;
        }
    }
}
