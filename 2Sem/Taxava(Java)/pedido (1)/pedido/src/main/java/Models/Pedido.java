package Models;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.math.BigDecimal;
import java.util.Date;
import java.util.List;

@Getter
@Setter
@Entity
@Table(name = "TBL_PEDIDO")
public class Pedido {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "ID_PEDIDO")
    private Long id;
    @Column(name = "DATA_PEDIDO")
    private Date dataPedido;
    @ManyToOne
    private Cliente cliente;
    @Column(name = "VALOR_TOTAL")
    private BigDecimal valorTotal;
}
