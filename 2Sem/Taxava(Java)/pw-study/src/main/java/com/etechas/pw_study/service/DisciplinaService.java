package com.etechas.pw_study.service;

import com.etechas.pw_study.entity.Disciplina;
import com.etechas.pw_study.repository.DisciplinaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.List;
import java.util.Optional;

@Service
public class DisciplinaService {
    @Autowired
    private DisciplinaRepository repository;

    public void cadastrarDisciplina(Disciplina disciplina){
        var existe = repository.findByNomeIgnoreCase(disciplina.getNome());
        if (existe.isEmpty())
            repository.save(disciplina);
        else
            throw new RuntimeException("Nome da disciplina já cadastada.");

    }

    public List<Disciplina> listar(){
        return repository.findAll();
    }

    public Optional<Disciplina> buscarPorId(Long id){
        var disciplina = repository.findById(id);
        return disciplina;
    }
}
