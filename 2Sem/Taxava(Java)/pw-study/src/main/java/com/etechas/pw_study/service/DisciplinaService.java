package com.etechas.pw_study.service;

import com.etechas.pw_study.entity.Disciplina;
import com.etechas.pw_study.repository.DisciplinaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class DisciplinaService {
    @Autowired
    private DisciplinaRepository repository;

    public void cadastrarDisciplina(Disciplina disciplina){
        repository.save(disciplina);
    }

}
