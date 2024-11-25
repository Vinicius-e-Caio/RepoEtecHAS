package Controllers;

import Models.Cliente;
import Models.Pedido;
import Services.ClienteService;
import Services.PedidoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/pedido")
public class PedidoController {

    @Autowired
    private PedidoService service;

    @PostMapping
    public ResponseEntity<Pedido> cadastrarPedido(@RequestBody Pedido pedido){

        var newPedido = service.cadastrarPedido(pedido);
        return ResponseEntity.status(HttpStatus.CREATED).body(newPedido);
    }

    @GetMapping("/listarPedido/{id}")
    public ResponseEntity<Pedido> buscarPedidos(@PathVariable Long id){
        var existe = service.listar(id);
        if (existe.isPresent()){
            return ResponseEntity.ok(existe.get());
        } else {
            return ResponseEntity.notFound().build();
        }
    }
}
