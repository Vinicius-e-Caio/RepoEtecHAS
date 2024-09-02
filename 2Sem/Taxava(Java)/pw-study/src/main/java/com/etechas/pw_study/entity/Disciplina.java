package com.etechas.pw_study.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
@Entity
@Table(name = "TBL_DISCIPLINA")
public class Disciplina {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "ID_DISCIPLINA")
    private Long id;

    @Column(name = "TX_NOME")
    private String nome;

}
