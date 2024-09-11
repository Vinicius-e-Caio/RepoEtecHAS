using CommunityToolkit.Mvvm.ComponentModel;
using HTTPClient.Models;
using HTTPClient.Services;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace HTTPClient.ViewModels
{
    public partial class TodoViewModel : ObservableObject
    {
        [ObservableProperty]
        ObservableCollection<Todo> todos;

        public ICommand getTodosCommand { get; }

        public TodoViewModel()
        {
            getTodosCommand = new Command(getTodos);
        }

        public async void getTodos()
        {
            TodoService todoService = new TodoService();
            Todos = await todoService.getTodos();
        }
    }
}
