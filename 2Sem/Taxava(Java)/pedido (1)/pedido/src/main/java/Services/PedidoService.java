package Services;

import Models.Pedido;
import Repository.PedidoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class PedidoService {
    @Autowired
    private PedidoRepository repository;


    public Pedido cadastrarPedido(Pedido pedido){
        var existFiveOrders = repository.findIdCliente(pedido.getCliente().getId());

        var existe = repository.findById(pedido.getId());
        if(existe.isEmpty())
            return repository.save(pedido);
        else
            throw new RuntimeException("Pedido com o mesmo ID!!!!");
    }
    public Optional<Pedido> listar(Long id){
        return repository.findIdCliente(id);
    }
}
