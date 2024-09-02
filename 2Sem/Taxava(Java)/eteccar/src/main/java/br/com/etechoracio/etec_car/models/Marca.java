package br.com.etechoracio.etec_car.models;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Entity
@Table(name = "TBL_MARCA")
public class Marca {
    // Definir que o mapeamento é da chave primária
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) // Identity
    @Column(name = "ID_MARCA")
    private Long id;
    @Column(name = "TX_NOME")
    private String nome;
}