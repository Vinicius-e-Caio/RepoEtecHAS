package br.com.etechoracio.etec_car.models;

import enums.TipoCombustivelEnum;
import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import org.hibernate.type.descriptor.jdbc.VarbinaryJdbcType;
import org.springframework.boot.context.properties.bind.Name;

import java.util.List;

@Getter
@Setter
@Entity
@Table(name = "TBL_AUTOMOVEL")
public class Automovel {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "ID_AUTOMOVEL")
    private Long id;

    @Column(name = "NR_ANO_FABRICACAO")
    private Integer anoFab;

    @Column(name = "NR_ANO_MODELO")
    private Integer anoMod;

    @Column(name = "TP_COMBUSTIVEL")
    @Enumerated(EnumType.STRING)
    private TipoCombustivelEnum combustivel;

    @Column(name = "NR_PRECO", columnDefinition = "numeric")
    private Double preco;

    @Column( name = "NR_KM_ATUAL")
    private Integer kmAtual;

    @ManyToOne
    @JoinColumn( name = "ID_MODELO")
    private Modelo modelo;

    @ManyToMany
    @JoinTable( name = "TBL_REL_AUTOMOVEL_ACESSORIO",
                joinColumns = @JoinColumn(name = "ID_AUTOMOVEL"),
                inverseJoinColumns = @JoinColumn(name = "ID_ACESSORIO")
    )

    private List<Acessorio> acessorios;
}
