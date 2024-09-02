package Models;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import org.hibernate.service.spi.InjectService;

@Getter
@Setter
@Entity
@Table(name = "TBL_PROJETO")
public class Projeto {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")

    private Long projetoID;

    @Column
    private Long funcionarioID;
}
