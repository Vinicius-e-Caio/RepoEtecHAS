package br.com.etechoracio.etec_car.models;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
@Entity
@Table(name = "TBL_MODELO")
public class Modelo {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "ID_MODELO")
    private Long id;

    @Column(name = "TX_NOME")
    private String nome;

    @Column(name = "NR_POTENCIA", columnDefinition = "numeric")
    private double nrPotencia;

    @ManyToOne
    @JoinColumn(name = "ID_MARCA")
    private Marca marca;
}
