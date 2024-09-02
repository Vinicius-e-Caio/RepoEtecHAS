package Models;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Entity
@Table(name = "TBL_Projeto_Funcionario")
public class projetoFuncionario {
    @Id
    @Column(name = "id")
    private Long id;

    @Column
    private String nome;
}
