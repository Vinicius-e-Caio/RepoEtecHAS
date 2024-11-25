package Services;

import Models.Cliente;
import Repository.ClienteRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ClienteService {
    @Autowired
    private ClienteRepository repository;

    public Cliente cadastrarCliente(Cliente cliente){
        var existe = repository.findById(cliente.getId());
        if (existe.isEmpty()){
            return repository.save(cliente);
        }
        else
            throw new RuntimeException("Cliente Já Cadastrado");
    }
}
